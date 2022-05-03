from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .forms import CustomerForm
from django.contrib import messages
#from django.shortcuts import render_to_response

# Create your views here.

def home_view(request):
    return render(request,'index.html',{})

def signup_view(request):
    submitted = False
    form = CustomerForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/signup_success')
        else:
            form = CustomerForm
            if 'submitted' in request.GET:
                submitted = True
            messages.info(request, 'That Username or Email is taken!')

    return render(request,'signup.html',{'form': form, 'submitted': submitted})

def signup_success_view(request):
    return render(request, 'signup_success.html', {}) #returns the index.html template

def login_view(request):
        form = CustomerForm()
        return render(request,'login.html',{'form': form})

def user_view(request):
    return render(request, 'user.html', {}) #returns the index.html template


def create_customer(request):
    form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})
