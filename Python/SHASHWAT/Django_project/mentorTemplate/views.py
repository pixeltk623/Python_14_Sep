from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
	#return HttpResponse("Hello, world. You're at the polls index.")
	return render(request, 'home.html', {'data': 'Home'})

def about(request):
	return render(request, 'about.html',{'data': 'About'})

def courses(request):
	return render(request, 'courses.html',{'data': 'Courses'})

def trainers(request):
	return render(request, 'trainers.html',{'data': 'Trainers'})

def events(request):
	return render(request, 'events.html',{'data': 'Events'})

def pricing(request):
	return render(request, 'pricing.html',{'data': 'Pricing'})

def contact(request):
	return render(request, 'contact.html',{'data': 'Contact'})

def courseDetails(request):
	return render(request, 'courseDetails.html',{'data': 'Courses'})

def base_call(request):
	return render(request, 'base.html')