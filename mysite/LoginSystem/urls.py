from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('store/', views.store, name='store'),
    path('user-login/', views.userLogin, name='userLogin'),
    path('validation/', views.validation, name='validation'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout_view'),

    path('relation/', views.relation),
]
