from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def register(request):
	return render(request, 'register.html')

def store(request):

	if request.method=='POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		username  = request.POST['username']
		password = request.POST['password']
		user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
		user.save()
		messages.success(request, 'Registration Done.')
	return redirect('http://127.0.0.1:8000/Login-system/')


def userLogin(request):
	return render(request, 'login.html')


def dashboard(request):
	return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/Login-system/user-login/')
    
def validation(request):
	if request.method=='POST':
		username  = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('http://127.0.0.1:8000/Login-system/dashboard/')
		else:
			messages.warning(request, 'Wrong Input.')
			return redirect('http://127.0.0.1:8000/Login-system/user-login/')
