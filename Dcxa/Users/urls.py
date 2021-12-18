from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('bank_details',views.bank_details)
]

