"""hum URL Configuration

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
#from . import views

from home.views import home_view, application_view
from login.views import login_view
from signup.views import signup_view #for multiple view import use {}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name ='home'),
    path('signup/', signup_view, name = 'signup'),
    path('login/', login_view, name = 'login'),
    path('application/', application_view, name='application'),
]# + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) #BS: for static files

urlpatterns += staticfiles_urlpatterns()

# url(r'^$', 'index', name='index'),
# url(r'^blog$', 'blog', name='blog'),



