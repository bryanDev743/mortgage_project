from django.shortcuts import render
#from django.shortcuts import render_to_response

# Create your views here.

def signup_view(request):
    return render(request,'signup.html',{})

def home_view(request):
    return render(request,'index.html',{})



# def signup_view(request):
#     return render_to_response('index.html')

