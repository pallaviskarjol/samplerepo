from django.shortcuts import render,redirect
from home.forms import *
from home.models import *
from django.contrib import messages


# Create your views here.
def  home_view(request):
	if request.method == 'POST':
		search =StudentSearchForm(request.POST)
		if search.is_valid():
			value = search.cleaned_data.get('q')
			result = Student.objects.filter(name__contains = value)
			return render(request,'home.html',{'result':result})
	else:
		form = StudentSearchForm()
		result = Student.objects.all()
		return render(request,'home.html',{'form':form})

	'''form = StudentSearchForm()
	context = {'form':form}
	return render(request,'home.html',context)'''

def contact(request):
    return render(request,'contact.html')

def about(request):
	form = AboutForm()
	context = {'form':form}
	return render(request,'about.html',context)

def delete_student(request,id):
	request.session['id'] = id
	result = Student.objects.get(id = id)
	result.delete()
	messages.success(request,"deleted successfully",)
	return redirect('/')

def edit_student(request,id):
	request.session['id'] = id
	student = Student.objects.get(id = id)
	if request.method == 'POST':
		modelform = StudentEditForm(request.POST,instance=student)
		if modelform.is_valid():
			modelform.save()
			return redirect('/')
	else:
		modelform = StudentEditForm(request.POST,instance=student)
		return render(request,'edit.html',{'form':modelform})
	messages.success(request,"changes saved successfully",)
	return redirect('/')

def createstudent(request):
	if request.method == "POST":
		form=StudentCreateForm(request.POST)
		if form.is_valid():
			# print("Branch = form.cleaned_data.get('Branch')",form.cleaned_data.get('Branch'))
			student=Student.objects.create(
				name=form.cleaned_data.get('name'),
				Branch = form.cleaned_data.get('Branch'))
			print('student',student)
			# student.save()
			messages.success(request,"created successfully")
			return redirect('/')
	else:
		form=StudentCreateForm()
		return render(request,'create.html',{'form':form,'value':'create'})