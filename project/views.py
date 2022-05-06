import django
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms
from .forms import CustomerForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib.auth import get_user_model
User = get_user_model()

from sklearn.tree import DecisionTreeClassifier
from pickle import load
#from django.shortcuts import render_to_response

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

from django.http import JsonResponse
from copy import copy
import pathlib
import numpy as np

def application_view(request):
    county_code_table = {'Suffolk County': 103,
                            'Queens County': 81,
                            'Kings County': 47,
                            'Nassau County': 59,
                            'Westchester County': 119,
                            'Erie County': 29,
                            'New York County': 61,
                            'Monroe County': 55,
                            'Bronx County': 5,
                            'Richmond County': 85,
                            'Orange County': 71,
                            'Onondaga County': 67,
                            'Dutchess County': 27,
                            'Saratoga County': 91,
                            'Albany County': 1,
                            'Rockland County': 87,
                            'Oneida County': 65,
                            'Niagara County': 63,
                            'Rensselaer County': 83,
                            'Schenectady County': 93,
                            'Ulster County': 111,
                            'Broome County': 7,
                            'Ontario County': 69,
                            'Jefferson County': 45,
                            'Putnam County': 79,
                            'Oswego County': 75,
                            'Wayne County': 117,
                            'Chautauqua County': 13,
                            'Steuben County': 101,
                            'Warren County': 113,
                            'Clinton County': 19,
                            'St. Lawrence County': 89,
                            'Sullivan County': 105,
                            'Washington County': 115,
                            'Chemung County': 15,
                            'Columbia County': 21,
                            'Cayuga County': 11,
                            'Otsego County': 77,
                            'Greene County': 39,
                            'Cattaraugus County': 9,
                            'Herkimer County': 43,
                            'Madison County': 53,
                            'Livingston County': 51,
                            'Chenango County': 17,
                            'Essex County': 31,
                            'Genesee County': 37,
                            'Tioga County': 107,
                            'Fulton County': 35,
                            'Delaware County': 25,
                            'Franklin County': 33,
                            'Orleans County': 73,
                            'Montgomery County': 57,
                            'Tompkins County': 109,
                            'Allegany County': 3,
                            'Cortland County': 23,
                            'Wyoming County': 121,
                            'Schoharie County': 95,
                            'Seneca County': 99,
                            'Lewis County': 49,
                            'Yates County': 123,
                            'Schuyler County': 97,
                            'Hamilton County': 41 }
    if request.method == "POST":
        p = copy(request.POST)
        name = p["search_name"]
        #return render(request, j, {})
        race_table = {"White": 5,
                      "African American": 3,
                      "Asian": 2,
                      "Native American/Alaskan Native": 1,
                      "Hawaiian/Pacific Islander": 4,
                      "Prefer not to say": 6}
        gender_table = {"Man": 1,
                        "Woman": 2,
                        "Prefer not to say": 3}
        r = {"race_id": race_table[p["search_race_lev"]]}
        g = {"gender_id": gender_table[p["search_gender_lev"]]}
        c = {"county_id": county_code_table[p["search_county"]]}
        p.update(r)
        p.update(g)
        p.update(c)
        # ["applicant_income_000s", "applicant_race_1", "applicant_sex", "application_date_indicator", "county_code", "property_type", "loan_amount_000s"]
       
        # Load decision tree
        path = pathlib.Path(__file__).parent.parent.absolute().as_posix()
        path = str(path)
        obj_path = path + "/static/ml_model/decision_tree_model.obj"
        with open(obj_path, "rb") as w:
            obj = load(w)

        # Create np array of data for use in the model
        arr = np.array([int(p["search_income"]) // 1000, p["race_id"], p["gender_id"], 0, p["county_id"], 1, int(p["search_loan"])//1000])
        # fake = np.array([25.0, 1, 1, 0, 55, 1, 125])
        status = obj.predict(arr.reshape(1, -1))
        status = status[0]
        status = int(status)
        p.update({"result": status})
        # print(obj.predict(fake.reshape(1, -1)))
        #return JsonResponse(p)
        # 2 or 6 approved, 3 denied
        return render(request, "results.html", {"result":status})

    c = sorted(list(county_code_table.keys()))
    context = {"county_codes": c}
    
    return render(request, "application.html", context)

def results_view(request):
    return render(request, "results.html", {"test":"red"})

#minute 41:32