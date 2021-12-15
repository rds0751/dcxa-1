from django.shortcuts import render

# Create your views here.

def signin(request):
    return render(request,'sign-in.html')
    
def signup(request):
    return render(request,'sign-up.html')    

def forgotpassword(request):
    return render(request, 'forgotpassword.html')

def loginwithotp(request):
    return render(request,"loginwithotp.html")

def dashboard(request):
    return render(request,"dashboard.html")

def update_profile(request):
    return render(request,"update_profile.html")

def change_password(request):
    return render(request,"change_password.html")

def buy_tokens(request):
    return render(request,"buy_tokens.html")
  
def add_new_person(request):
    return render(request,"add_new_person.html")

def buy_wallet(request):
    return render(request,"buy_wallet.html")
def directteam(request):
    return render (request, "Directteam.html")
def levelview(request):
    return render(request,"levelteam.html")
def roiview(request):
    return render(request,'roiview.html')
def allteammember(request):
    return render(request,'allteam.html')
def treeview(request):
    return render(request,"teamview.html")
def wallet_transfer(request):
    return render(request,"wallet_transfer.html")