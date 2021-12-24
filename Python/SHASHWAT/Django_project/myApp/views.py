from django.shortcuts import render
from django.http import HttpResponse
from .models import Crud
from django.shortcuts import redirect  
from django.contrib import messages
import datetime
import pytz
import os
import time

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

		if 'gender' in request.POST:
			gender = request.POST['gender']
		else:
			gender = ''

		if 'hobbies' in request.POST:
			hobby = request.POST.getlist('hobbies')
			hobby = ','.join(hobby)
		else:
			hobby = ''

		if 'city' in request.POST:
			cityName = request.POST['city']
		else:
			cityName = ''
		
		

		if 'uploadFile' in request.FILES:
			print(request.FILES)

			profile_pic = request.FILES['uploadFile']
			splitName = os.path.splitext(profile_pic.name)
			fileName = str(int(time.time()))+splitName[1]
			handle_uploaded_file(profile_pic, fileName)
		else:
			fileName = ''
	

		if Name != '' and Email !='' and Mobile !='' and cityName != '' and gender !='' and hobby != '':
			res = Crud(name=Name, email=Email, mobile = Mobile, gender=gender, hobbies=hobby, cityName=cityName,profile_pic=fileName)
			res.save()
			messages.add_message(request, messages.INFO, 'New User Added')
			return redirect('/')  
		else:
			messages.add_message(request, messages.INFO, 'Error')
			return redirect("/create")  

def handle_uploaded_file(f, fileName):
    with open('myApp/static/upload/'+fileName, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def edit(request, id):
	single_data = Crud.objects.get(pk=id)
	return render(request, 'edit.html',{'single_data' : single_data})

def update(request):
	b = Crud.objects.get(pk=request.POST['uid'])

	Name = request.POST['name']
	Email = request.POST['email']
	Mobile = request.POST['mobile']

	if 'gender' in request.POST:
		gender = request.POST['gender']
	else:
		gender = ''

	if 'hobbies' in request.POST:
		hobby = request.POST.getlist('hobbies')
		hobby = ','.join(hobby)
	else:
		hobby = ''

	if 'city' in request.POST:
		cityName = request.POST['city']
	else:
		cityName = ''
	if 'uploadFile' in request.FILES:
		profile_pic = request.FILES['profile_pic']
		splitText  = os.path.splitext(profile_pic.name)
		fileName = str(int(time.time()))+splitText[1]
		handle_uploaded_file(profile_pic, fileName)
	else:
		fileName = ''

	if Name != '' and Email !='' and Mobile !='' and cityName != '' and gender !='' and hobby != '':
		b.name = Name
		b.email = Email
		b.mobile = Mobile
		b.gender = gender
		b.hobbies = hobby
		b.cityName = cityName
		b.profile_pic = fileName
		b.modified_date = datetime.datetime.now()
		b.save()
		messages.add_message(request, messages.INFO, 'User Updated')
		return redirect('/')
	else: 
		messages.add_message(request, messages.INFO, 'Error')
		return redirect('/edit')  

def show(request,id):
	single_data = Crud.objects.get(pk=id)
	return render(request, 'show.html',{'single_data' : single_data})

def delete(request, id):
	b = Crud.objects.get(pk=id)
	b.delete()
	if b.profile_pic:
		os.remove('myApp/static/upload/'+b.profile_pic)
	messages.add_message(request, messages.INFO, 'User Deleted')
	return redirect('/')