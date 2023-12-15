from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name = "home page"),
    path('BTC_Data',views.alldata,name = "table"),
    path('Bitcoin',views.g1,name = "g1"),
    path('Ethereum', views.g2, name="g2"),
    path('Matic', views.g3, name="g3"),
    path('Volume', views.g4, name="g4"),
    path('Turnover', views.g5, name="g5"),
    ]