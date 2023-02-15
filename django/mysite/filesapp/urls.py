
# -*- coding: utf-8 -*-
from django.urls import path, re_path

import filesapp

from . import views

urlpatterns = [
    path('', views.index, name='filesapp_index'),
]