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