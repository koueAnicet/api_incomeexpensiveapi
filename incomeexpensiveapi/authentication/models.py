from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.


class UserManager(BaseUserManager):
    
    def create_user(self, username, email, password=None):
        
        if username is None:
            raise TypeError("Users should have a username")
        if email is None:
            raise TypeError("Users should have a email")
        if username is None:
            raise TypeError("Users should have a username")
        
        user = self.model(
            username=username,
            email=self.email_normalize, 
        )
        user.set_password(password)
        user.save()
        
    def create_superuser(self, username, email, password=None):
            
        if password is None:
            raise TypeError("Password should be a none")
       
        user = self.create_user(
            username,
            email, 
            password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    eamil = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    USER_NAME_FIELD = 'email' #la constante avec se connecter 
    REQUIRED_FIELD = ['username'] #les champs obligatoir a entrer a connections
    
    objects = UserManager()
    
    def __str__(self):
        return self.eamil
    
    def tokens(self):
        return ''
    