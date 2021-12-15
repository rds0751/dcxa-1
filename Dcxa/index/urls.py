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
    path('wallet_statement/',views.wallet_statement),
    path('income_details/',views.income_details),
    path('investment_details/',views.investment_details),
    path('buy_tokens/',views.buy_tokens),
    path('admin/',admin.site.urls),
    path('directteam/',views.directteam),
    path('levelview/', views.levelview),
    path('roiview/', views.roiview),
     path('wallet_transfer/', views.wallet_transfer),
    path('allteammember/', views.allteammember),
    path('treeview/', views.treeview),
    path('buysip/',views.buysip),
    path('buyproperty',views.buyproperty),
    path('forex',views.forex),
    path('ticket',views.ticket)
]
