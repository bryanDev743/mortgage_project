"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings #BS: for static files
from django.conf.urls.static import static #BS: for static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name ='home'),
    path('signup', views.signup_view, name = 'signup'),
    path('signout', views.sign_out, name = 'signout'),
    path('login', views.login_view, name = 'login'),
    path('login1', views.login1_view, name = 'login1'),
    #path('home', views.login_view, name = 'signout'),
    path('user', views.user_view, name = 'user'),
    path('customer_form', views.create_customer, name='create_customer'),
]# + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) #BS: for static files
