from django.shortcuts import render
# Create your views here.
from django.db import models
from .models import Profile
from .models import Bank_Details
from django.contrib.auth.models import User

def bank_details(request):
    username=request.user.username
    print(request.POST)
    if request.method=="POST":
        account_no=request.POST.get('account_no')
        confirm_account_no=request.POST.get('confirm_account_no')
        ifsc_code=request.POST.get('ifsc_code')
        iban_no=request.POST.get('iban_no')
        swift_code= request.POST.get('swift_code')
        passbook=request.FILES.get('passbook')
        obj= Bank_Details(account_no=account_no, confirm_account_no=confirm_account_no, ifsc_code=ifsc_code, iban_no=iban_no, swift_code=swift_code,passbook=passbook)
        obj.save()
    return render(request,"dashboard.html")
