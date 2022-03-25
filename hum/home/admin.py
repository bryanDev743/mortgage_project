from django.contrib import admin
from .models import User, Finance, Bank, Loan, User_has_Loan, Bank_offers_Loan

myModels = [User, Finance, Bank, Loan, User_has_Loan, Bank_offers_Loan]

admin.site.register(myModels)
#admin.site.register(Loan, User_has_Loan, Bank_offers_Loan)

# Register your models here.
