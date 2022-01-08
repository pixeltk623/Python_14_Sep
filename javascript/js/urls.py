from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allData', views.getAllData, name='all'),
    path('insertData', views.insertDataAll, name = 'insert'),
    path('deleteData', views.deleteData, name = 'delete'),
]
