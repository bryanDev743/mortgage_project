from django.urls import path
from . import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login_user', views.login_user, name="login"),
    path('signup_user', views.signup_user, name="signup"),
]# + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) #BS: for static files
