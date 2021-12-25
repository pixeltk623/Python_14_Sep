from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('store/', views.store, name='store'),
    path('delete/<int:id>/', views.delete, name='delete'),

    path('file', views.fileUpload, name='file_upload'),

]
