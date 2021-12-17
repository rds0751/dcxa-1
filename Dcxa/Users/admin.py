from django.contrib import admin

# Register your models here.
from users.models import Profile
from users.models import Kyc

admin.site.register(Profile)
admin.site.register(Kyc)