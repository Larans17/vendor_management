from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from VendorAPI.serializers.login import *
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

# KNOX TOKEN
from knox.auth import AuthToken


# CUSTOM METHODS
from VendorAPI.utils import *
from VendorAPI.common.common_methods import *


# LOGIN FUNCTION ::
class LoginAPI(APIView):
    """
        Summary or Description of the Function:
            * Log-in SuperAdmin.
    """
    def post(self, request, *args, **kwargs):      
        try:
            serializer_class = LoginSerializer(data=request.data, context={'request': request})
            if serializer_class.is_valid():
                callbulkCreation(),
                data = doAdminLogin(serializer_class, request)
                return Response(data,status.HTTP_200_OK)
            else:
                return VendorAPIResponse.serializer_error(self.__class__.__name__, request, serializer_class)
            
        except Exception as e:
            return VendorAPIResponse.exception_error(self.__class__.__name__, request, e)

def doAdminLogin(serializer_class, request):
    user = serializer_class.validated_data['user']
    token = AuthToken.objects.create(user)[1]
    user_data = getObject(User,{'user_name':user})
    displayname=user_data.user_name if user_data.is_super_admin else user_data.display_name
    if user_data.is_super_admin:
        data={  
            'user_id':user_data.id,
            'display_name':displayname,
            'is_super_admin':user_data.is_super_admin,
            'emailId':user_data.email,
            "message": LOGIN_VERIFIED,
            "Token": token,
        }
    
    return data