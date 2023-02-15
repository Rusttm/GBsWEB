
# -*- coding: utf-8 -*-
from django.urls import path, re_path


from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='filesapp_index'),
    path('upload/', views.file_upload_view),
    path('filesapp/upload/', views.file_upload_view),
]