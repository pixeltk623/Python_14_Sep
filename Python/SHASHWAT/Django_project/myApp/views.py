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

		if Name != '' and Email !='' and Mobile !='' and cityName != '' and gender !='' and hobby != '' :
			res = Crud(name=Name, email=Email, mobile = Mobile, gender=gender, hobbies=hobby, cityName=cityName)
			res.save()
			messages.add_message(request, messages.INFO, 'New User Added')
			return redirect('/')  
		else:
			messages.add_message(request, messages.INFO, 'Error')
			return redirect("/create")  


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

	if Name != '' and Email !='' and Mobile !='' and cityName != '' and gender !='' and hobby != '' :
		b.name = Name
		b.email = Email
		b.mobile = Mobile
		b.gender = gender
		b.hobbies = hobby
		b.cityName = cityName
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
	messages.add_message(request, messages.INFO, 'User Deleted')
	return redirect('/')