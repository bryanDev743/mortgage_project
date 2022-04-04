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

class Finance(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    race = models.CharField(max_length=25, default='SOME STRING')
    gender = models.CharField(max_length=10, default='SOME STRING')
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


