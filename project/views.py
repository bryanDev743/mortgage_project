from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .forms import ClientForm
from django.contrib import messages
#from django.shortcuts import render_to_response

# Create your views here.

def home_view(request):
    return render(request,'index.html',{})

# def signup_view(request):
#     submitted = False
#     form = ClientForm(request.POST)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/signup_success')
#         else:
#             form = ClientForm
#             if 'submitted' in request.GET:
#                 submitted = True
#             messages.info(request, 'That Username or Email is taken!')
#
#     return render(request,'signup.html',{'form': form, 'submitted': submitted})

# Using old signup as new database entry

def new_client_view(request):
    submitted = False
    form = ClientForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful Client Registry!')
            return HttpResponseRedirect('/new_client')
        else:
            form = ClientForm
            if 'submitted' in request.GET:
                submitted = True
            messages.info(request, 'That Username or Email is taken!')

    return render(request,'new_client.html',{'form': form, 'submitted': submitted})

def signup_success_view(request):
    return render(request, 'signup_success.html', {}) #returns the index.html template

def login_view(request):
        form = ClientForm()
        return render(request,'login.html',{'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout Successful!')
    return render(request, 'home.html', {})

def user_view(request):
    return render(request, 'user.html', {}) #returns the index.html template
