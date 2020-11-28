from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('connect/', views.connect, name='connect'),
]