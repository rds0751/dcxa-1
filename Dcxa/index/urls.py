from django.contrib import admin
from django.urls import path
from index import views

urlpatterns = [
    path('', views.signin),
    path('signup/',views.signup),
    path('forgotpassword/',views.forgotpassword),
    path('loginwithotp/',views.loginwithotp),
    path('admin/',admin.site.urls)
]