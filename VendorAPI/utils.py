from VendorAPI.models import *

#  THIRD PARTY PACKAGE IMPORT
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import traceback


from rest_framework.response import Response
from rest_framework import status
import traceback
import uuid
from datetime import datetime
from django.db.models import Count,Avg
from django.utils import timezone

from rest_framework.response import Response
from rest_framework import status

def getFirstObject(model):
    return model.objects.first()

def getLastObject(model):
    return model.objects.last()

def getAllObject(model):
    return model.objects.all()

def getAllObjectWithFilter(model, filter_params={}):
    return model.objects.filter(**filter_params)

def getObject(model, filter_params={}):
    return model.objects.get(**filter_params)


def getCode(type):

    new_uuid = uuid.uuid1()

    # Convert the UUID to an integer and take modulo to get a 5-digit number
    five_digit_number = int(new_uuid) % 100000
    two_digit_number = int(new_uuid) % 100
    current_year = datetime.now().year
    match type:
        case "vendor":
            code = "VEN" + str(five_digit_number)
        case "porder":
            code = "PONO" + str(two_digit_number)+ str(current_year)
    return code

def Log(transaction_name, msg, Ip, Mode=None, userid=None):
    import socket
    HOSTNAME = socket.gethostname()
    Logs.objects.create(
        transaction_name=transaction_name, mode=Mode, log_message=str(msg),
        userid_id=userid,system_name=HOSTNAME, ip_address=Ip
        )

class VendorAPIResponse:
    
    @staticmethod
    def serializer_error(className, request, serializer, user_id=None):

        Ip = request.META['REMOTE_ADDR']
        msg = {'status': status.HTTP_400_BAD_REQUEST,'message': serializer.errors}
        Log(className, msg, Ip, request.method, user_id)
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    
    @staticmethod
    def transaction_error(className, request, error, user_id=None):
        Ip = request.META['REMOTE_ADDR']
        msg = {'status': status.HTTP_400_BAD_REQUEST,'message': error}
        Log(className, msg, Ip, request.method, user_id)
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    
    @staticmethod
    def exception_error(className, request, e, user_id=None):
        log_msg={'error':str(e),'traceback':traceback.format_exc()}
        Ip = request.META['REMOTE_ADDR']
        mode = None
        Log(className, log_msg, Ip, request.method, user_id)
        error = {'status':status.HTTP_400_BAD_REQUEST, 'message' : 'Something went wrong!'}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    
    @staticmethod
    def restricted_error(className, request, errorName, user_id=None):
        Ip = request.META['REMOTE_ADDR']
        error_message = f'{errorName} is being referenced with another instance'
       
        error_data = {'status': status.HTTP_409_CONFLICT, 'message': error_message}
        Log(className, request.method, error_data, Ip, user_id)


    @staticmethod
    def validation_error(msg, user_status):
        error_data = {'status':user_status, 'message': msg}
        return Response(error_data, status=status.HTTP_400_BAD_REQUEST)
    

def update_vendor_performance_metrics(vendor):
    completed_po = getAllObjectWithFilter(PurchaseOrder,{'vendor':vendor,'status':2})
    on_time_deliveries = completed_po.filter(delivery_date__gte = timezone.now())

    vendor.on_time_delivery_rate = on_time_deliveries.count()\
          /completed_po.count() * 100 if completed_po.count() > 0 else 0
    completed_po_with_ratings = completed_po.exclude(quality_rating__isnull = True)

    vendor.quality_rating_avg = completed_po_with_ratings.aggregate(Avg('quality_rating'))\
        ['quality_rating__avg'] or 0
    
    acknowledged_pos = completed_po.filter(acknowledgment_date__isnull=False)
    response_times = [(po.acknowledgment_date - po.issue_date).total_seconds() for po in acknowledged_pos]
    vendor.average_response_time = sum(response_times) / acknowledged_pos.count() if acknowledged_pos.count() > 0 else 0

    completed_po_without_issues = completed_po.filter(status=2)
    vendor.fulfillment_rate = (completed_po_without_issues.count() / completed_po.count()) * 100 if completed_po.count() > 0 else 0

    vendor.save()
