from django.shortcuts import render
from django.http import JsonResponse
from .models import Ajax
# Create your views here.

def index(request):
	return render(request, 'index.html')

def getAllData(request):
	all_entries = Ajax.objects.values()
	all_entries = list(all_entries) # Remove QuerySet
	return JsonResponse({'data': all_entries})	


def insertDataAll(request):

	if request.method=='POST':
		name = request.POST['name']
		email = request.POST['email']
		mobile = request.POST['mobile']
		gender = request.POST['gender']

		if name != '' and email !='' and mobile !='' and gender !='':
			res = Ajax(name=name, email=email, mobile = mobile, gender=gender)
			res.save()
			return JsonResponse({'status': True})	
		else:
			return JsonResponse({'status': False})

		

def deleteData(request):
	if request.method=='GET':
		did = int(request.GET['id'])
		b = Ajax.objects.get(pk=did)
		b.delete()
		return JsonResponse({'status': True})