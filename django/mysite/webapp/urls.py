
# -*- coding: utf-8 -*-
from django.urls import path
# import re_path as url from django.urls
from django.urls import url
import webapp

from . import views

urlpatterns = [
    path('', views.index, name='webapp/index'),
    path('example', views.example_page, name='webapp/example'),
    path('file', views.upload_file, name='uploader'),
    url(r'^list/$',webapp.views, name='list'),

]