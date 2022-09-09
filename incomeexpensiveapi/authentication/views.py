from urllib import request
from django.shortcuts import render
from rest_framework import generics, status

from .serializers import RegisterSerialier
from rest_framework.response import Response


class RegisterView(generics.GenericAPIView):
    serializers_class = RegisterSerialier
    
    def post(self, request):
        user = request.data
        serializer = self.serializers_class(
            data=user
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)