# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='matplotapp'),
    path('index', views.index, name='matplotapp_index'),

]