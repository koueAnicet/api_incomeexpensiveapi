import email
from urllib import request
from django.shortcuts import render
from rest_framework import generics, status

from .serializers import RegisterSerialier
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
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
        
        user = User.objects.get( email=user_data['email'])
        token = RefreshToken.for_user(user).access_token #pour donner le token
        
        current_site = get_current_site(request).domain
        relativLink = reverse('email-verify')
        absurl ='https://'+current_site+relativLink+"?token="+str(token)
        email_body='Hi '+ user.username +' Use the link for verify your email \n'+ absurl
        data = {'email_body':email_body,'to_email': user.email, 'email_subjet':'Verify your email'}
        Util.send_email(data)
        
        return Response(user_data, status=status.HTTP_201_CREATED)
    
class VerifyEmail(generics.GenericAPIView):
    def get(self,):
        pass