from django.shortcuts import render
# Create your views here.
from django.db import models
from .models import Profile
from django.contrib.auth.models import User

# def signup(request):
#     if request.method=='POST':
#         name = request.POST.get('textname')
#         email = request.POST.get('txtemail')
#         mobile = request.POST.get('txtmobile')
#         firstpw = request.POST.get('textpwd')
#         secondpw = request.POST.get('textcheckpwd')
#         if firstpw==secondpw:
#             p = User.objects.create_user(name,email,firstpw)
#             p.save()
#         return render(request,'dashboard.html')
