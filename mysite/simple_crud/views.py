from django.shortcuts import render
from django.http import HttpResponse
from .models import Crud
from django.shortcuts import redirect  
from django.contrib import messages

# Create your views here.

def index(request):
	return render(request, 'index.html')

def create(request):
	return render(request, 'create.html')

def store(request):
	
	if request.method=='POST':
		name = request.POST['name']
		email = request.POST['email']
		mobile = request.POST['mobile']
		res = Crud(name=name, email=email, mobile = mobile)
		res.save()
	messages.add_message(request, messages.INFO, 'New User Added')
	return redirect('/simple_crud')  