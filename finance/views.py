from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import*
from django.views.generic import TemplateView

# Create your views here.


class LoginView(TemplateView):
    template_name='finance/login.html'

class Registerationform(TemplateView):
    template_name = 'finance/signup.html'




class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)