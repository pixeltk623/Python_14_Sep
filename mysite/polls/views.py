from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
	#return HttpResponse("Hello, world. You're at the polls index.")
	return render(request, 'polls/index.html', {'data': 'Home'})

def about(request):
	return render(request, 'polls/about.html',{'data': 'About'})
def courses(request):
	return render(request, 'polls/courses.html',{'data': 'Courses'})
def trainers(request):
	return render(request, 'polls/trainers.html',{'data': 'Trainers'})
def events(request):
	return render(request, 'polls/events.html',{'data': 'Events'})
def pricing(request):
	return render(request, 'polls/pricing.html',{'data': 'Pricing'})
def contact(request):
	return render(request, 'polls/contact.html',{'data': 'Contact'})

def base_call(request):
	return render(request, 'polls/base.html')