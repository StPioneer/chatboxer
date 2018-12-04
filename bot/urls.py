# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 20:30:18 2018

@author: StPioneer
"""
from django.conf.urls import include, url
from bot import views

urlpatterns = [
    url('^callback/', views.callback, name='callback'),
]
