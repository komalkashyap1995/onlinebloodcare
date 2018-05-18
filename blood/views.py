# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# from.forms import feedback_form, register_form, story_form, userform
from blood.forms import (
	 contact_form,
	 # register_form,
	 story_form,
	 # RegistrationForm, 
	 # EditProfileForm
	 LoginForm
	
    ) 
from.models import *
from django.http import HttpResponseRedirect
from django.db.models import Q
# from django.http import HttpRedirect
from django.http import *
from .models import User, inspiringstories
# from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib import auth
# from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
# from django.views.generic import ListView, CreateView, UpdateView

# Create your views here.
def index(request):
	return render(request,'index.html')
def base(request):
	return render(request,'base.html')
def tipsondonating(request):
	return render(request,'tips on donating.html')
def whoneedsblood(request):
	return render(request,'who needs blood.html')
def whocanorcantdonateblood(request):
	return render(request,'Who can or cant donate blood.html')
def bloodimportance(request):
	return render(request,'Blood importance.html')
def mostneededblood(request):
	return render(request,'Most needed blood.html')
def blooddonationfacts(request):
	return render(request,'blood donation facts.html')
def about(request):
	return render(request,'about.html')
def footer(request):
	return render(request,'footer.html')
def termsofuse(request):
	return render(request,'terms of use.html')
def faq(request):
	return render(request,'faq.html')
def contactus (request):
	if request.method == 'POST':
		form = contact_form(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Thank You, you successfully submitted your feedback')
			return HttpResponseRedirect('../contactus/')
			# return HttpResponse("request received")
	else:
		form = contact_form()
	return render(request,'Contact us.html', {'form':form})

def whydonateblood(request):
	return render(request,'why donate blood.html')
def privacypolicy(request):
	return render(request,'privacy policy.html')
def bloodchain(request):
	return render(request,'Blood chain.html')
# def registration(request):
# 	if request.method == 'POST':
# 		form = register_form(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return "request received"
			
# 	else:
# 		form = register_form()
# 	return render(request, 'register.html', {'form':form})

def stories(request):
	if request.method == 'POST':
		form = story_form(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Dear user, you successfully submitted your story')
			return HttpResponseRedirect('../inspiringstories/')
	else:
		form = story_form()
	return render(request, 'inspiring stories.html', {'form':form})

# def list_i(request):
# 	products = inspiringstories.objects.all()
# 	return render(request,'inspiring stories.html', {'products':products})


# def register(request): 
# 	if request.method == 'POST':
# 		form1 =  RegistrationForm(request.POST)
# 		if form1.is_valid():
# 			form1.save()
# 			return HttpResponseRedirect('/blood/login/')
# 	else:
# 	    form1 = RegistrationForm()
# 	    args = {'form':form1}
# 	return render(request, 'registration.html', args)    		
	
	# This frm is key used in registration.html

# def registration(request):
# 	if request.method == 'POST':
# 		form = userform(request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data['username']
# 			first_name = form.cleaned_data['first_name']
# 			last_name = form.cleaned_data['last_name']
# 			email = form.cleaned_data['email']
# 			password = form.cleaned_data['password']
# 			User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
# 	     	messages.success(request,'user registration success')
# 		    return HttpResponse("user created")
# 	else:
# 		form = userform()
# 	return render(request,'registration.html',{'form':form})

# def login(request):
# 	if request.method == 'POST':
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		try:
# 			user = auth.authenticate(username = username, password = password)
# 			if user is not None:
# 				auth.login(request, user)
# 				return render(request, 'about.html')
# 			else:
# 				messages.error(request,'username and password did not match')
# 		except auth.ObjectNotExist:
# 			print("invalid user")
# 	# return render(request, 'login.html', {'form':form})
# 	return render(request, 'login.html')

# def profile(request):
# 	args = {'user': request.user}
# 	return render(request, 'profile.html', args)

# def edit_profile(request):
# 	if request.method =='POST': 
# 		form = EditProfileForm(request.POST, instance=request.user) 

# 		if form.is_valid():
# 			form.save() 
# 			return redirect('/blood/profile') 
# 	else:
# 		form = EditProfileForm(instance=request.user) 
# 		args = {'form': form} 
#  		return render(request, 'edit_profile.html', args) 

# def change_password(request):
# 	if request.method =='POST':
# 		form = PasswordChangeForm(data=request.POST, user=request.user)

# 		if form.is_valid():
# 			form.save()
# 			update_session_auth_hash(request, form.user)
# 			messages.success(request, 'Your password was successfully updated!')
# 			return redirect('/blood/profile')
			
# 			# return "password changed"
# 	else:
# 		form = PasswordChangeForm(user=request.user)
# 		args = {'form': form}
# 		return render(request, 'change_password.html', args)
          
# def logout(request):
# 	return redirect('index' )

def signup(request):
	if request.session.has_key('username'):
		return redirect('userlogin')
	else:
		msg =''
		if request.method == 'POST':
			name = request.POST['name']
			Email= request.POST['Email']			
			Password = request.POST['Password']
			Confirm_Password = request.POST['Confirm_Password']
			Weight = request.POST['Weight']
			Age = request.POST['Age']
			Gender = request.POST['Gender']
			Phone_Mobile = request.POST['Phone_Mobile']
			Phone_Office = request.POST['Phone_Office']
			Country = request.POST['Country']
			City = request.POST['City']
			State = request.POST['State']
			District = request.POST['District']
			Blood_Group = request.POST['Blood_Group']
			user = User(name=name)
			user.Email = Email
			user.Password = Password
			user.Confirm_Password = Confirm_Password
			user.Weight = Weight
			user.Age = Age
			user.Gender = Gender
			user.Phone_Mobile = Phone_Mobile
			user.Phone_Office = Phone_Office
			user.Country = Country
			user.City = City
			user.Blood_Group = Blood_Group
		
			user.save()
			msg="Successfully Registered ! Login Now"

		return render(request, 'register.html',{'Msg': msg})
			
	# if request.session.has_key('username'):
		# return redirect('userlogin')
	
	# else:
	# 	msg =''
	# 	if request.method == 'POST':
	# 		name = request.POST['name']
	# 		Email= request.POST['Email']			
	# 		Password = request.POST['Password']
	# 		Confirm_Password = request.POST['Confirm_Password']
	# 		Weight = request.POST['Weight']
	# 		Age = request.POST['Age']
	# 		Gender = request.POST['Gender']
	# 		Phone_Mobile = request.POST['Phone_Mobile']
	# 		Phone_Office = request.POST['Phone_Office']
	# 		Country = request.POST['Country']
	# 		Pincode = request.POST['Pincode']
	# 		Blood_Group = request.POST['Blood_Group']
	# 		user = User(name=name)
	# 		user.Email = Email
	# 		user.Password = Password
	# 		user.Confirm_Password = Confirm_Password
	# 		user.Weight = Weight
	# 		user.Age = Age
	# 		user.Gender = Gender
	# 		user.Phone_Mobile = Phone_Mobile
	# 		user.Phone_Office = Phone_Office
	# 		user.Country = Country
	# 		user.Pincode = Pincode
	# 		user.Blood_Group = Blood_Group
		
	# 		user.save()
	# 		msg="Successfully Registered ! Login Now"

	# 	return render(request, 'register.html',{'Msg': msg})

	# if request.session.has_key('username'):
	# 	return redirect('userlogin')
	
	# else:
		

def signin(request):
	username = ""
	if request.method == 'POST':
		Email = request.POST['Email']
		Password = request.POST['Password']
		user = User.objects.filter(Email=Email,Password=Password)

		if not user:
			username ='Invalid login'
			template='login.html'
		else:
			template='userlogin.html'
			username=Email
			request.session['username']=username
			
	else:
		template = 'login.html'

	return render(request, template, {'username': username})

# def userlogin(request):
# 	if request.session.has_key('username'):
# 		template = 'userlogin.html'
# 		contacts = User.objects.all()
# 		return render(request, template, {'contacts': contacts})
		
# 	else:
# 		template = 'login.html'
# 		return render(request, template,{})
	
	# return render(request, 'userlogin.html')

# def update_profile(request, id):
#     user = User.objects.get(id=id)
#     form = SignupForm(request.POST or None, instance=user)

#     if form.is_valid():
#          form.save()	
#          return redirect('userlogin')

#     return render(request, 'userlogin.html', {'form': form, 'user': user})

def userlogin(request):
	if request.session.has_key('username'):
		srch = request.session['username']

		if srch:
			match = User.objects.filter(Email__iexact=srch)
			if match:
				return render(request,'userlogin.html', {'rs':match})
			else:
				messages.error(request,'no results found')
		else:
			return HttpResponseRedirect('/userlogin/')

	return render(request,'userlogin.html')


def search(request):
	if request.method == 'POST':
		srch = request.POST['bg']

		if srch:
			match = User.objects.filter(Q(Blood_Group__iexact=srch) | Q(District__iexact=srch) | Q(City__iexact=srch))
			if match:
				return render(request,'search.html', {'sr':match})
			else:
				messages.error(request,'no results found')

		else:
			return HttpResponseRedirect('/search/')

	return render(request,'search.html')

def contact_view(request):
	contacts = feedback.objects.all()
	return render(request,'views.html', {'contacts': contacts})

# def pagelogout(request):
# 	if request.method == "POST":
# 		logout(request)

# 		return redirect('index')


# def logout(request):
# 	try:
# 		del request.session['username']
# 	except KeyError:
# 		pass
# 	return HttpResponse("You're logged out.")




