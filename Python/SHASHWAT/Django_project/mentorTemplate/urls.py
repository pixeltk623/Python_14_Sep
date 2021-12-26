from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('trainers/', views.trainers, name='trainers'),
    path('events/', views.events, name='events'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('base/', views.base_call, name='base'),
    path('course-details/', views.courseDetails, name='course-details'),
]