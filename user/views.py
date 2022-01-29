from django.shortcuts import render
from user import serializers
from user.models import AccountModel
from rest_framework.views import APIView
from user.serializers import RegistrationSeializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user import models

# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSeializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration Successful!"
            data['email'] = account.email

            token = Token.objects.get(user=account).key
            data['token'] = token

        else:
            data = serializer.errors

        return Response(data)
