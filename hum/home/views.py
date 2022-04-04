from django.shortcuts import render
from .models import User

def home_view(request):

    #alldata = User.objects.all

    return render(request,'index.html',{})


def application_view(request):

    #alldata = User.objects.all

    return render(request,'application.html',{})




#def 
# Create your views here.
