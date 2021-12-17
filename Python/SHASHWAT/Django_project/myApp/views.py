from django.shortcuts import render
from django.http import HttpResponse
from .models import Crud
from django.shortcuts import redirect  
from django.contrib import messages
import datetime
import pytz

def index(request):
	all_entries = Crud.objects.all()
	print(all_entries)
	return render(request, 'index.html', {'all_entries' : all_entries})

def create(request):
    return render(request,'create.html')

def store(request):
	# return HttpResponse("STORE")

	if request.method=='POST':
		Name = request.POST['name']
		Email = request.POST['email']
		Mobile = request.POST['mobile']
		gender = request.POST['gender']
		hobby = request.POST.getlist('hobbies')
		hobby = ','.join(hobby)
	
		cityName = request.POST['city']
		res = Crud(name=Name, email=Email, mobile = Mobile, gender=gender, hobbies=hobby, cityName=cityName)
		res.save()
	messages.add_message(request, messages.INFO, 'New User Added')
	return redirect('/')  

def edit(request, id):
	single_data = Crud.objects.get(pk=id)
	return render(request, 'edit.html',{'single_data' : single_data})

def update(request):
	b = Crud.objects.get(pk=request.POST['uid'])
	b.name = request.POST['name']
	b.email = request.POST['email']
	b.mobile = request.POST['mobile']
	b.modified_date = datetime.datetime.now()
	b.save()
	messages.add_message(request, messages.INFO, 'User Updated')
	return redirect('/')    

def show(request,id):
	single_data = Crud.objects.get(pk=id)
	return render(request, 'show.html',{'single_data' : single_data})

def delete(request, id):
	b = Crud.objects.get(pk=id)
	b.delete()
	messages.add_message(request, messages.INFO, 'User Deleted')
	return redirect('/')