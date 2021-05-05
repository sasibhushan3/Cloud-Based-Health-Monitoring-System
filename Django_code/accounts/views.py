from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def register(request):
	return render(request,'register.html')

def userdata(request):
	first = request.GET.get('first')
	last = request.GET.get('last')
	user = request.GET.get('user')
	pas = request.GET.get('pass')
	email = request.GET.get('email')

	if User.objects.filter(username=user).exists():
		# print(1)
		messages.info(request,'Username exists')
		return redirect('login')
	else:
		# print(2)
		user1 = User.objects.create_user(username=user,password=pas,email=email,first_name=first,last_name=last)
		user1.save()
		# print(3)
		request.session['user']=user
		request.session['pass']=pas
		return redirect('health_checkup')


def login(request):
	print(request.method)
	if request.method=='POST':
		use = request.POST.get('user')
		pas = request.POST.get('pass')

		user = auth.authenticate(username=use,password=pas)
		if user is not None:
			print(1)
			request.session['user']=use 
			request.session['pass']=pas
			auth.login(request,user)
			return redirect('health_checkup')
		else:
			print(2)
			messages.info(request,'Invalid credentials')
			return redirect('login')

	else:
		print(3)
		return render(request,'login.html')