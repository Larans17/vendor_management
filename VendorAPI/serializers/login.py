#DJANGO DEFAULT PACKAGE IMPORT
from VendorAPI.models import *
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import serializers
from VendorAPI.common.api_response_message import *
from VendorAPI.utils import *



class LoginSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label=("password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=125,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'user_name', 'password']


    def validate(self, data):
        Username = data.get('user_name')
        Password = data.get('password')
        if Username and Password:
            user = getAllObjectWithFilter(User,{'user_name':Username}).first()
            
            if user is None:
                raise serializers.ValidationError({'Username':INVALID_USERNAME}, CODE)
            
            if not check_password(Password, user.password):
                raise serializers.ValidationError({'Password':INVALID_PASSWORD}, CODE)
        else:
            raise serializers.ValidationError(VALIDATION_MSG, CODE)

        data['user'] = user
        return data