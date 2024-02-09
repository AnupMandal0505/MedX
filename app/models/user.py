from django.db import models
from django.utils import timezone

from .manager import UserManager

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from autoslug import AutoSlugField



# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=225,blank=True, default='', unique=True)
    email = models.EmailField(blank=True, default='', unique=True)
    first_name = models.CharField(max_length=225, blank=True, default='')
    last_name = models.CharField(max_length=225, blank=True, default='')
    city = models.CharField(max_length=255, blank=True)
    user_type = models.CharField(max_length=255, blank=True)
    status = models.IntegerField(default=0, blank=True)
    profile = models.FileField(upload_to='profile/',max_length=250,blank=True,null=True,default=None)
    delete = models.BooleanField(default=False)
    phone_slug=AutoSlugField(populate_from='email',
                         unique_with=['first_name', 'last_name'],null=True,default=None)
    



    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    object = UserManager()
    

    USERNAME_FIELD = 'phone'
    EMAIL_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return self.first_name
    
    def get_short_name(self):
        return self.first_name or self.email.split('@')[0]
    
    


    
    
