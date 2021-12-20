from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect  
from django.contrib import messages
import datetime
import pytz
from .models import Complex

def index(request):
	all_entries = Complex.objects.all()
	print(all_entries)
	return render(request, 'complex/index.html', {'all_entries' : all_entries})

def create(request):
	#return HttpResponse("Hello")
	return render(request, 'complex/create.html')


def store(request):

	if request.method=='POST':
		name = request.POST['name']
		email = request.POST['email']
		mobile = request.POST['mobile']
		if 'gender' in request.POST:
			gender = request.POST['gender']
		else:
			gender = ''
		if 'hobby' in request.POST:
			hobby = request.POST.getlist('hobby')
			hobby = ','.join(hobby)
		else:
			hobby = ''
		city = request.POST['city']
		
		if name != '' and email !='' and mobile !='' and city != '' and gender !='' and hobby != '':
			res = Complex(name=name,email=email,mobile=mobile,gender=gender,hobby=hobby,city=city)
			res.save()
			messages.add_message(request, messages.INFO, 'Added')
			return redirect('/complex_crud') 
		else:
			messages.add_message(request, messages.INFO, 'Error')
			return redirect('/complex_crud/create') 



def delete(request, id):
	b = Complex.objects.get(pk=id)
	b.delete()
	messages.add_message(request, messages.INFO, 'User Deleted')
	return redirect('/complex_crud')

def show(request, id):
	single_data = Complex.objects.get(pk=id)
	return render(request, 'complex/show.html',{'single_data' : single_data})


def edit(request, id):
	single_data = Complex.objects.get(pk=id)
	return render(request, 'complex/edit.html',{'single_data' : single_data})


def update(request):
	b = Complex.objects.get(pk=request.POST['uid'])
	name = request.POST['name']
	email = request.POST['email']
	mobile = request.POST['mobile']
	if 'gender' in request.POST:
		gender = request.POST['gender']
	else:
		gender = ''
	if 'hobby' in request.POST:
		hobby = request.POST.getlist('hobby')
		hobby = ','.join(hobby)
	else:
		hobby = ''
	city = request.POST['city']

	if name != '' and email !='' and mobile !='' and city != '' and gender !='' and hobby != '':
		b.name = request.POST['name']
		b.email = request.POST['email']
		b.mobile = request.POST['mobile']
		b.modified_date = datetime.datetime.now()
		b.gender = gender
		b.city = city
		b.hobby = hobby
		b.save()
		messages.add_message(request, messages.INFO, 'User Updated')
		return redirect('/complex_crud') 
	else:
		messages.add_message(request, messages.INFO, 'Error')
		return redirect('/complex_crud/edit')  