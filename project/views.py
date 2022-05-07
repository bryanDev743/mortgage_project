import django

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

def login_view(request):
        form = ClientForm()
        return render(request,'login.html',{'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout Successful!')
    return render(request, 'home.html', {})

def user_view(request):
    return render(request, 'user.html', {}) #returns the index.html template

from django.http import JsonResponse
from copy import copy
import pathlib
import numpy as np
from pickle import load

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
