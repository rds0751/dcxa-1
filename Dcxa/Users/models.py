from django.db import models
from datetime import datetime

class profile(models.Model):
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
    card_number = models.IntegerField()
    

class KYC(models.Model):
    username = models.ForeignKey(profile, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    photo = models.FileField(upload_to='photo/')
    livephoto = models.FileField(upload_to='livephoto')
    documentname = models.CharField(max_length= 255)
    documentid = models.CharField(max_length=255)
    documentfront = models.FileField(upload_to='documentfront')
    documentback = models.FileField(upload_to='documentback')
    


