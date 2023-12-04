from VendorAPI.models import *
from VendorAPI.serializers.vendor import *
from django.db import transaction
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import json
from django.db.models import RestrictedError

# KNOX TOKEN
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from VendorAPI.common.api_response_message import *
from VendorAPI.common.common_methods import *
from VendorAPI.utils import *




class VendorPostAPI(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        """
        Summary or Description of the function:
            Post Vendor data to database.

        """
        try:
            data = request.data.copy()
            data['vendor_code'] = getCode('vendor')
            serializer_class = PostVendorSerializer(data = data,context={'request':request})
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data,status=status.HTTP_201_CREATED)
            else:
                return Response(
                        serializer_class.errors, status=status.HTTP_400_BAD_REQUEST
                    )
        except Exception as e:
            return VendorAPIResponse.exception_error(self.__class__.__name__, request, e)
        

    def get(self,request,*args,**kwargs):
        """
        Summary or Description of the function:
            Get all vendor list data from database.

        """
        try:
            queryset = getAllObject(Vendor)
            serializer_class = PostVendorSerializer(queryset,many=True,context={'request':request})
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return VendorAPIResponse.exception_error(self.__class__.__name__, request, e)
        

class VendorPutAPI(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self,request,vendorid,**kwargs):
        """
        Summary or Description of the function:
            Get all vendor list data from database.

        """
        try:
            queryset = getObject(Vendor,{'vendorid':vendorid})
            serializer_class = GetAllVendorSerializer(queryset,context={'request':request})
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return VendorAPIResponse.exception_error(self.__class__.__name__, request, e)
        

    def put(self,request,vendorid,**kwargs):
        """
        Summary or Description of the function:
            put vendor details vendorid based.

        """
        try:
            queryset = getObject(Vendor,{'vendorid':vendorid})
            serializer_class = UpdateVendorSerializer(queryset,data=request.data,context={'request':request},partial=True)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data,status=status.HTTP_201_CREATED)
            else:
                return Response(
                        serializer_class.errors, status=status.HTTP_400_BAD_REQUEST
                    )
        except Exception as e:
            return VendorAPIResponse.exception_error(self.__class__.__name__, request, e)
        
    def delete(self,request,vendorid,**kwargs):
        """
        Summary or Description of the function:
            delete vendor details by vendorid based.

        """
        try:
            query_set = getAllObjectWithFilter(Vendor,{'vendorid':vendorid})
            if query_set.exists():
                query_set.delete()
            

                response_data = {
                    "message": CommonApiMessages.delete("Vendor"),
                    "status": status.HTTP_200_OK,
                }
            return Response(
                data=response_data,
                status=status.HTTP_200_OK,
            )

        except RestrictedError:
            return Response(
                data=CommonApiMessages.restrict_delete("Vendor"),
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        except Exception as e:
            return VendorAPIResponse.exception_error(self.__class__.__name__, request, e)
        



#    PURCHASE ORDER APIS

class PuchaseOrderPostAPI(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        """
        Summary or Description of the function:
            Post purchase order data to database.

        """
        try:
            data = request.data.copy()
            data['po_number'] = getCode('porder')
            serializer_class = PostPurchaseOrderSerializer(data = data,context={'request':request})
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data,status=status.HTTP_201_CREATED)
            else:
                return Response(
                        serializer_class.errors, status=status.HTTP_400_BAD_REQUEST
                    )
        except Exception as e:
            return VendorAPIResponse.exception_error(self.__class__.__name__, request, e)
        

    def get(self,request,*args,**kwargs):
        """
        Summary or Description of the function:
            Get all purchase order list data from database.

        """
        try:
            queryset = getAllObject(PurchaseOrder)
            serializer_class = GetPurchaseOrderSerializer(queryset,many=True,context={'request':request})
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return VendorAPIResponse.exception_error(self.__class__.__name__, request, e)
        

class PurchaseOrderPutAPI(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self,request,poid,**kwargs):
        """
        Summary or Description of the function:
            Get all purchase order list data from database.

        """
        try:
            queryset = getObject(PurchaseOrder,{'poid':poid})
            serializer_class = GetPurchaseOrderSerializer(queryset,context={'request':request})
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return VendorAPIResponse.exception_error(self.__class__.__name__, request, e)
        

    def put(self,request,poid,**kwargs):
        """
        Summary or Description of the function:
            Update purchase order details poid based.

        """
        try:
            queryset = getObject(PurchaseOrder,{'poid':poid})
            serializer_class = PostPurchaseOrderSerializer(queryset,data=request.data,context={'request':request},partial=True)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data,status=status.HTTP_201_CREATED)
            else:
                return Response(
                        serializer_class.errors, status=status.HTTP_400_BAD_REQUEST
                    )
        except Exception as e:
            return VendorAPIResponse.exception_error(self.__class__.__name__, request, e)
        
        
    def delete(self,request,poid,**kwargs):
        """
        Summary or Description of the function:
            delete purchase order details by poid based.

        """
        try:
            query_set = getAllObjectWithFilter(PurchaseOrder,{'poid':poid})
            print(query_set)
            if query_set.exists():
                query_set.delete()
            

                response_data = {
                    "message": CommonApiMessages.delete("Purchase order"),
                    "status": status.HTTP_200_OK,
                }
            return Response(
                data=response_data,
                status=status.HTTP_200_OK,
            )

        except RestrictedError:
            return Response(
                data=CommonApiMessages.restrict_delete("Purchase order"),
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        except Exception as e:
            return VendorAPIResponse.exception_error(self.__class__.__name__, request, e)