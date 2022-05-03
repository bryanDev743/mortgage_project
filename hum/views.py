from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms
from .forms import CustomerForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

def home_view(request):
    return render(request,'index.html',{})

def signup_view(request):

    if request.method == "POST":
        #username = request.POST.get('uname')
        username = request.POST['uname']
        fname = request.POST['user_fname']
        lname = request.POST['user_lname']

        email = request.POST['user_email']
        email1 = request.POST['user_email1']

        password = request.POST['user_password']
        password1 = request.POST['user_password1']

        zipcode = request.POST['zipcode']
        phone = request.POST['phone']

        if User.objects.filter(username=username):
            messages.error(request," User already exists")
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request," Email already in use")
            return redirect('signup')

        if User.objects.filter(phone=phone):
            messages.error(request," Phone number already in use")
            return redirect('signup')

        if len(username) > 50 :
            messages.error(request," Username too big")
            return redirect('signup')

        if password != password1:
            messages.error(request," Password don't match")
            return redirect('signup')

        if email != email1:
            messages.error(request," Emails don't match")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request," Username must be alphanumeric")
            return redirect('signup')


        #myUser = User.objects.create_user(fname=fname,lname=lname,username=username,email=email,password=password,zipcode=zic)
        myUser = User.objects.create_user(fname,lname,username,email,password,zipcode,phone)
        # myUser.fname = fname
        # myUser.lname = lname
        # myUser.zipcode = zipcode
        # myUser.phone = phone

        myUser.save()
        messages.success(request, " Account Created, Welcome!")

        return redirect('home')
    

    return render(request,'signup.html',{})

def login_view(request):
        form = CustomerForm()
        return render(request,'login.html',{'form': form})

def login1_view(request):
        if  request.method == "POST":
            username = request.POST.get('user_name')
            #username = request.POST['user_name']
            passw1 = request.POST.get('passw1')

            user = authenticate(request,username=username, password=passw1)

            if user is not None:
                login(request,user)
                fname = user.fname
                return render(request, 'home', {'fname':fname})

            else:
                messages.error(request,"Bad credentials")
                return redirect('login1')

        return render(request,'login1.html',{})

def user_view(request):
    return render(request, 'user.html', {}) #returns the index.html template


def create_customer(request):
    form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

def sign_out(request):
    logout(request)
    messages.success(" Goodbye")
    return render(request,'index.html',{})


#minute 41:32