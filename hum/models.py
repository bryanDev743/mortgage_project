from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)


# from django.contrib.auth import get_user_model
# User = get_user_model()


class UserManager(BaseUserManager):
    def create_user(self,fname,lname,username,email, password, zipcode,phone, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username ')
        if not fname:
            raise ValueError('Users must have a First Name ')
        if not lname:
            raise ValueError('Users must have an Last Name ')
        if not password:
            raise ValueError('Users must have an Password ')
        if not phone:
            raise ValueError('Users must have a Phone number ')
        if not zipcode:
            raise ValueError('Users must have a zipcode ')

        now = timezone.now()
        #email = self.normalize_email(email)
        user = self.model(
            fname=fname,
            lname=lname,
            username=username,
            email=self.normalize_email(email),
            zipcode=zipcode, 
            phone=phone ,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,fname,lname,username,email, password, zipcode,phone, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an email address')

        now = timezone.now()
        user = self.create_user(
            fname=fname,
            lname=lname,
            password=password,
            username=username,
            email=self.normalize_email(email),
            zipcode=zipcode, 
            phone=phone ,
            **extra_fields
        )
    
        is_staff = True
        is_superuser = True
        is_active = True
        user.save(using=self._db)

        return user

    

    # def create_user(self, email, password, **extra_fields):
    #     return self._create_user(email, password, False, False, **extra_fields)


class User(AbstractBaseUser):
    #REQUIRED_FIELDS = ('username',)

    #username = models.OneToOneField(User, related_name='profile', unique=True)

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=50)
    #states = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    #dob = models.CharField(max_length=15)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['fname','lname','email', 'password', 'zipcode','phone']

    objects = UserManager()

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def __str__(self):
        return self.fname


class Finance(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    credit_score = models.IntegerField()
    credit_line = models.IntegerField()
    income = models.IntegerField()
    budget = models.IntegerField()
    debts = models.IntegerField()

class Bank(models.Model):
    bank_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    states = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=9)
    routing_number = models.IntegerField()

class Loan(models.Model):
    interest = models.IntegerField()

class User_has_Loan(models.Model):
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 

class Bank_offers_Loan(models.Model):
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE) 
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE) 


#https://medium.com/@royprins/django-custom-user-model-email-authentication-d3e89d36210f


# Create your models here.

# class User(models.Model):
#     REQUIRED_FIELDS = ('username',)

#     #username = models.OneToOneField(User, related_name='profile', unique=True)

#     fname = models.CharField(max_length=50)
#     lname = models.CharField(max_length=50)
#     username = models.CharField(max_length=50)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=50)
#     states = models.CharField(max_length=50)
#     zipcode = models.CharField(max_length=10)
#     phone_n = models.CharField(max_length=15)
#     dob = models.CharField(max_length=15)

    

#     #return names in admin
#     # def__str__(self):
#     #     return self.uname + ' ' + self.email


