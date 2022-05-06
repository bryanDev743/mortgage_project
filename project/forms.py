from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Crispy forms imports
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from models.models import *


# Create your forms here.



class ClientForm(ModelForm):
	class Meta:
			model = User
			fields = ("fname", "lname", "uname", "email", "passw", "states", "zipcode", "phone_n", "dob")

			labels = {
				'fname': '',
				'lname': '',
				'uname': '',
				'email': '',
				'passw': '',
				'states': '',
				'zipcode': '',
				'phone_n': '',
				'dob': '',
			}

			widgets = {
				'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
				'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
				'uname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
				'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
				'passw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
				'states': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
				'zipcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
				'phone_n': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
				'dob': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
			}

#def save(self, commit=True):
#		user = super(NewUserForm, self).save(commit=False)
#		user.email = self.cleaned_data['email']
#		if commit:
#			user.save()
#		return user
