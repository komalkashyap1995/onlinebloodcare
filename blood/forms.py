from __future__ import unicode_literals

from django import forms
from.models import *
from blood.models import User
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

COUNTRY_CHOICES = [
	('in', 'India'),
    # ('ca', 'Canada'),
   	]

GENDER_CHOICES=[
	('male','Male'),
	('female','Female'),
	]

BLOOD_CHOICES=[
	('A+','A+'),
	('A-','A-'),
	('B+','B+'),
	('B-','B-'),
	('AB+','AB+'),
	('AB-','AB-'),
	('O+','O+'),
	('O-','O-'),
]	
 # favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))

# class register_form(forms.ModelForm):
# 	Email = forms.EmailField(label='email', max_length=100)
# 	Name = forms.CharField(label='Your name', max_length=100)
# 	Password = forms.CharField(label='Your password', max_length=200)
# 	Confirm_Password = forms.CharField(label='Confirm password', max_length=200)
# 	Weight = forms.FloatField(label='Your weight')
# 	Age = forms.IntegerField(label='age')
# 	Gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER_CHOICES))
# 	Phone_Mobile = forms.IntegerField(label='Your mobileno')
# 	Phone_Office = forms.IntegerField(label='Your officeno')
# 	# Country = forms.CharField(label='Your countrty', max_length=50)
# 	Country = forms.CharField(widget=forms.Select(choices=COUNTRY_CHOICES))
# 	Pincode = forms.IntegerField(label='pincode')
# 	Blood_Group = forms.CharField(widget=forms.Select(choices=BLOOD_CHOICES))

# 	class Meta():
# 		model = donorregistration
# 		fields = ['Email','Password','Confirm_Password','Name','Gender','Weight','Age','Phone_Mobile','Phone_Office','Country','Pincode', 'Blood_Group']

class contact_form(forms.ModelForm):
	Name = forms.CharField(label='Name', required=True, max_length=100)
	Email = forms.EmailField(label='Email', required=True, max_length=100)
	Message = forms.CharField(label='Message',widget=forms.Textarea(attrs={"rows":5, "cols":20}), required=True, max_length=100)

	class Meta():
		model = feedback
		fields = ['Name','Email','Message']


# class feedback_form(forms.ModelForm):
# 	Name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}), required=True, max_length=100)
# 	Email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Emailid'}),required=True)
# 	Message=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your messaage'}), required=True, max_length=100)

# 	class Meta():
# 		model = feedback
# 		fields = ['Name','Email','Message']

# comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20})

class story_form(forms.ModelForm):
	First_name = forms.CharField(label='First name', required=True, max_length=30)
	Last_name = forms.CharField(label='Last name', max_length=30)
	Email = forms.EmailField(label='Email', max_length=100)
	Mobile = forms.IntegerField(label='Mobile')
	Story = forms.CharField(label='Story', widget=forms.Textarea(attrs={"rows":5, "cols":30}), required=True)

	class Meta():
		model = inspiringstories
		fields = ['First_name','Last_name','Email','Mobile','Story']

# class userform(forms.ModelForm):
# 	username = forms.CharField(widget=forms.TextInput)
# 	email = forms.EmailField(widget=forms.EmailInput)
# 	first_name = forms.CharField(widget=forms.TextInput)
# 	last_name = forms.CharField(widget=forms.TextInput)
# 	password = forms.CharField(widget=forms.PasswordInput)
	
# 	class Meta():
# 		model = User
# 		fields = ['username','email','first_name','last_name','password']

# class RegistrationForm(UserCreationForm):
# 	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}), required=True, max_length=100)
# 	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}), required=True, max_length=50)
# 	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Firstname'}), required=True, max_length=100)
# 	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your lastname'}), required=True, max_length=100)
# 	#password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}), required=True, max_length=100)
# 	#confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}), required=True, max_length=100)

# 	class Meta():
# 		model = User
# 		fields = ['username','email','first_name','last_name']

# class EditProfileForm(UserChangeForm):
# 	username = forms.CharField(required=True)
# 	email = forms.EmailField(required=True)
# 	first_name = forms.CharField(required=False)
# 	last_name = forms.CharField(required=False)

# 	class Meta:
# 		model = User
# 		fields = ['username','email','first_name','last_name', 'password']

class LoginForm(forms.Form):
	User = forms.CharField(max_length = 100)
	Password = forms.CharField(widget = forms.PasswordInput())

	def clean_message(self):
		username = self.cleaned_data.get("username")
		dbuser = User.objects.filter(name = username)
		if not dbuser:
			raise forms.ValidationError("User does not exist in our db!")
		return username

class SignupForm(forms.Form):
	name = forms.CharField(max_length = 100)
	Email = forms.CharField(max_length=100)
	Password = forms.CharField(widget=forms.PasswordInput)
	Confirm_Password = forms.CharField(widget=forms.PasswordInput)
	Weight = forms.FloatField()
	Age = forms.IntegerField(label='age')
	Gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER_CHOICES))
	Phone_Mobile = forms.IntegerField(label='Your mobileno')
	Phone_Office = forms.IntegerField(label='Your officeno')
	Country = forms.CharField(widget=forms.Select(choices=COUNTRY_CHOICES))
	City = forms.CharField(label='city')
	Blood_Group = forms.CharField(widget=forms.Select(choices=BLOOD_CHOICES))
	State = forms.CharField(max_length=20)
	District = forms.CharField(max_length=20)


	# class Meta:
	# 	model = User
	# 	fields = ['name','Email','Password','Weight','Age','Gender','Phone_Mobile','Phone_Office','Country','Pincode','Blood_Group']
	
	






