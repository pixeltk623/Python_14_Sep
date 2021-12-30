from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='Product'),
    path('final-payment/', views.payment, name='Payment'),
    path('card-details/', views.CardDetails, name='CardDetails'),
    path('charge', views.PaymentDone, name='PaymentDone'),
]
