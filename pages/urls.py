# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 21:53:58 2023

@author: waterfall
"""
from django.urls import path
from . import views

urlpatterns = [   
    path('', views.home, name="home")
]