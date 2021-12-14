from django.contrib import admin
from django.urls import path
from index import views

urlpatterns = [
    path('', views.signin),
    path('signup/',views.signup),
    path('forgotpassword/',views.forgotpassword),
    path('loginwithotp/',views.loginwithotp),
    path('dashboard/',views.dashboard),
    path('update_profile/',views.update_profile),
    path('add_new_person/',views.add_new_person),
    path('admin/',admin.site.urls)
]