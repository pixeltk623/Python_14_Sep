from django.shortcuts import render,redirect
from django.http import HttpResponse
import time
import os
from .models import FileUpload


# Create your views here.


def index(request):
	all_entries = FileUpload.objects.all()
	print(all_entries)
	return render(request, 'fileUpload/index.html', {'all_entries' : all_entries})


def create(request):
	return render(request, 'fileUpload/create.html')

def store(request):
	if request.method=='POST':
		return HttpResponse(request.FILES['profile_pic'].size)
		name = request.POST['name']

		if 'profile_pic' in request.FILES:
			profile_pic  = request.FILES['profile_pic']
			splitText  = os.path.splitext(profile_pic.name)
			
			ext = splitText[1].lower().replace('.', '')

			if ext=='jpg' or ext=='png' or ext=='jpeg':
				print("Valid")
			else:
				print("Not Valid")

			print(profile_pic._size)


			return HttpResponse("Hello")
			fileName = str(int(time.time()))+splitText[1]
			handle_uploaded_file(profile_pic, fileName)
		else:
			fileName = ''
		
		res = FileUpload(name=name,profile_pic=fileName)
		res.save()
		return redirect('/file-upload') 
		
def handle_uploaded_file(f, fileName):
    with open('FileUpload/static/upload/'+fileName, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def delete(request, id):
	b = FileUpload.objects.get(pk=id)
	print(b.profile_pic)
	b.delete()
	os.remove('FileUpload/static/upload/'+b.profile_pic)
	return redirect('/file-upload')


def fileUpload(request):
	if request.method=='POST':
		print(request.FILES['profile_pic'].size)
	return render(request, 'fileUpload/file.html')