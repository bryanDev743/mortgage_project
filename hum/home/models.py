from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    uname = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    passw = models.CharField(max_length=50)
    states = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_n = models.CharField(max_length=15)
    dob = models.CharField(max_length=15)

    #return names in admin
    # def__str__(self):
    #     return self.uname + ' ' + self.email


