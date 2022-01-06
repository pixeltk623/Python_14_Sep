from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Main'),
    path('create', views.create, name='Form'),
]
