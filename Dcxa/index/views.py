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
  
def add_new_person(request):
    return render(request,"add_new_person.html")

def buy_wallet(request):
    return render(request,"buy_wallet.html")

def wallet_statement(request):
    return render(request,"wallet_statement.html")

def income_details(request):
    return render(request,"income_details.html")

def investment_details(request):
    return render(request,"investment_details.html")