from django.contrib import admin
from django.urls import path
from index import views

urlpatterns = [
    path('', views.signin),
    path('signup/',views.signup),
    path('admin/',admin.site.urls)
]