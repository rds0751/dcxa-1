from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager

class Profile(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=25, primary_key=True)
    full_name = models.CharField(max_length=255)
    mobile = models.CharField(unique=False,max_length=15)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    is_superuser = models.BooleanField(blank=True, default=False)
    profile_pic = models.FileField(upload_to='profile_pics/', null=True)
    referral = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    card_number = models.IntegerField(null=True,default=0)
    

class Kyc(models.Model):
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    photo = models.FileField(upload_to='photo/')
    livephoto = models.FileField(upload_to='livephoto')
    documentname = models.CharField(max_length= 255)
    documentid = models.CharField(max_length=255)
    documentfront = models.FileField(upload_to='documentfront')
    documentback = models.FileField(upload_to='documentback')
    

class Bank_Details(models.Model):
    # username = models.ForeignKey(profile, on_delete=models.CASCADE)
    account_no = models.CharField(max_length=30)
    confirm_account_no = models.CharField(max_length=30)
    ifsc_code = models.CharField(max_length=30)
    iban_no = models.CharField(max_length=30)
    swift_code = models.CharField(max_length=30)
    passbook= models.FileField(upload_to='passbook/',null=False)    

