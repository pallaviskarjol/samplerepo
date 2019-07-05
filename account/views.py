from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,logout,login
from .forms import userRegisterForm

# Create your views here.

def home_view(request):
	return render(request,'testpage.html')
 
def user_login(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				return redirect('/')
			else:
				return HttpResponse("your account was inactive")
		else:
			print('someone tried to login and failed')
			print('they used username:{} and password:{}'.format(username,password))
	else:
		return render(request,'auth/login.html')

def user_logout(request):
	logout(request)
	return redirect('/')

def register(request):
	registered = False
	if request.method == "POST":
		user_form =userRegisterForm(request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print(user_form.errors)
	else:
		user_form = userRegisterForm()
	return render(request,'auth/register.html',{'form':user_form,'registered':registered})
