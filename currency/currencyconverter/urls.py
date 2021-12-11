from django.contrib import admin
from django.urls import path
from currencyconverter.views import *

urlpatterns = [
     path('',index),
    path('dashboard/',dashboard),
    path('login/',login),
    path('loginaction/',loginAction),
    path('logout/',logoutAction),
    path('signup/',signup),
    path('signupaction/',signupaction),
    path('currencyconverter/',convert),
    # path('open/',showlist),
    # path('account/', openaccount),
    # path('delete/<str:account>',deletecustomer),
    # path('view/<str:account>',viewcustomer),
    # path('showlist/',showlist),
    # path('search/', search),
    # path('searchpage/', searchpage),
    path('transfer/', transfer),
    path('showtransferresult/', showtransferresult),
    # path('withdraw/',withdraw),
    # path('withdrawamount/',withdrawamount),
    # path('statementresult/',statementresult),
    # path('statement/',statement),
    # path('deposite/',deposite),
    # path('depositeresult/',depositeresult),


]