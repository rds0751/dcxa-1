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
    path('change_password/',views.change_password),
    path('add_new_person/',views.add_new_person),
    path('buy_wallet/',views.buy_wallet),
    path('buy_tokens/',views.buy_tokens),
    path('admin/',admin.site.urls)
]