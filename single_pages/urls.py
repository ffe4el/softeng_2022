from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.landing_page),
    path('about_me/', views.about_me),
]
