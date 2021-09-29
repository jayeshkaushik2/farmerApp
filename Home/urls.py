from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tractorsList', views.tractorsList, name='tractorsList'),
    path('farmerpage/', views.farmerpage, name='farmerpage'),
    path('farmerpage/<str:username>/', views.farmerpage, name='farmerpage'),
]