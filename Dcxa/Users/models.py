from django.db import models

class KYC(models.models):
    username = models.ForeignKey(profile, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    photo = models.FileField(upload_to='photo/')
    livephoto = models.FileField(upload_to='livephoto')
    documentname = models.CharField(max_length= 255)
    documentid = models.CharField(max_length=255)
    documentfront = models.FileField(upload_to='documentfront')
    documentback = models.FileField(upload_to='documentback')
    




    
