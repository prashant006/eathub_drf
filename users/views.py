from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Customer, RestaurantOwner
from .import serializers
# Create your views here.

class CustomerSignupApi(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializers


class CustomerProfileUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerProfileSerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


# class CustomerPasswordUpdate(generics.UpdateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = serializers.CustomerPasswordUpdateSerializers
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

class CustomerPasswordUpdate(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def patch(self, request, *args, **kwargs):
        user = request.user
        serializer = serializers.CustomerPasswordUpdateSerializers(user,data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save() 
            return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MyTokenObtainPairviewApi(TokenObtainPairView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]


class RestaurantOwnerSignupApi(generics.CreateAPIView):
    queryset = RestaurantOwner.objects.all()
    serializer_class = serializers.RestaurantOwnerSerializers


class RestaurantOwnerProfileUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantOwner.objects.all()
    serializer_class = serializers.RestaurantOwnerProfileSerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class RestaurantOwnerPasswordUpdate(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def patch(self, request, *args, **kwargs):
        user = request.user
        serializer = serializers.RestaurantOwnerPasswordUpdateSerializers(user,data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save() 
            return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    