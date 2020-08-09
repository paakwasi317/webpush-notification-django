from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
from datetime import datetime 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import PermissionsMixin

class MyAccountManager(BaseUserManager):
    def _create_user(self, email, password,**extraarguments):
        if not email:
            raise ValueError('User must have an email address')
        if not password:
            raise ValueError('User must have a password')

        user = self.model(
            email = self.normalize_email(email),
             **extraarguments
        )

        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        print('this is the password')
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self,email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username

        )

        user.is_admin = False
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_company(self, email=None, password=None, **extra_fields):
        print('this is the password')
        return self._create_user(email, password, **extra_fields)




class Users(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    firstname = models.CharField(max_length=60, default=None, null=True)
    lastname = models.CharField(max_length=60, default=None, null=True)
    othernames = models.CharField(max_length=60, default=None, null=True)
    username = models.CharField(max_length=60, default=None, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    isadmin = models.IntegerField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    phone = models.CharField(max_length=60, unique=True)
    referral_code = models.CharField(max_length=60, default=None, null=True, blank=True)
    location = models.CharField(max_length=100)
    profilepic = models.ImageField(upload_to="images/userlogo/", null=True, blank=True)
    code = models.CharField(max_length=10, default="0000", null=True)
    objects = MyAccountManager()

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.email


