from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .forms import CustomerForm
#from django.shortcuts import render_to_response

# Create your views here.

def home_view(request):
    return render(request,'index.html',{})

def signup_view(request):
    return render(request,'signup.html',{})

def login_view(request):
        form = CustomerForm()
        return render(request,'login.html',{'form': form})

def user_view(request):
    return render(request, 'user.html', {}) #returns the index.html template


def create_customer(request):
    form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})
