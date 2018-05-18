# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django import forms
from django.forms import ModelForm
# from django.contrib.auth.models import User

# Create your models here.
# class donorregistration(models.Model):
# 	Email=models.EmailField()
# 	Name=models.CharField(max_length=50)
# 	Password=models.CharField(max_length=8)
# 	Confirm_Password=models.CharField(max_length=8)
# 	Weight=models.FloatField(max_length=3)
# 	Gender=models.CharField(max_length=10)
# 	Age=models.IntegerField(max_length=3, default='18')
# 	Phone_Mobile=models.CharField(max_length=10)
# 	Phone_Office=models.CharField(max_length=10)
# 	Country=models.CharField(max_length=10)
# 	Pincode=models.IntegerField(max_length=10, default='123')
# 	Blood_Group=models.CharField(max_length=10, default='123')

# 	def __str__(self):
# 		return self.Email

class feedback(models.Model):
	Name=models.CharField(max_length=50)
	Email=models.EmailField()
	Message=models.CharField(max_length=300)

	def __str__(self):
		return self.Name

	
class inspiringstories(models.Model):
	First_name=models.CharField(max_length=30)
	Last_name=models.CharField(max_length=30)
	Email=models.EmailField()
	Mobile=models.IntegerField()
	Story=models.CharField(max_length=600)

	def __str__(self):
		return self.First_name

class User(models.Model):
	name=models.CharField(max_length=50)
	Email=models.EmailField()
	Password=models.CharField(max_length=8)
	Confirm_Password=models.CharField(max_length=8)
	Weight=models.FloatField()
	Gender=models.CharField(max_length=10)
	Age=models.IntegerField(default='18')
	Phone_Mobile=models.CharField(max_length=10)
	Phone_Office=models.CharField(max_length=10)
	Country=models.CharField(max_length=10)
	City=models.CharField(max_length=10, default='pathankot')
	Blood_Group=models.CharField(max_length=10, default='123')
	State=models.CharField(max_length=20, default='punjab')
	District=models.CharField(max_length=20, default='pathankot')












# model for signup
# class signup(models.Model):                                  
# 	username = models.CharField(max_length=50)
# 	email = models.EmailField(max_length=50)
# 	first_name = models.CharField(max_length=100)
# 	last_name = models.CharField(max_length=100)
# 	password = models.CharField(max_length=100)
# 	confirm_password = models.CharField(max_length=100)
	
	

	# def __str__(self): #__unicode__(self):
	# 	return self.username





        