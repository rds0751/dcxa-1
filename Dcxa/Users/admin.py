from django.contrib import admin

# Register your models here.
from users.models import profile
from users.models import KYC

admin.site.register(profile)
admin.site.register(KYC)