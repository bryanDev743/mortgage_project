from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from .models import User, Finance, Bank, Loan, User_has_Loan, Bank_offers_Loan
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

myModels = [User, Finance, Bank, Loan, User_has_Loan, Bank_offers_Loan]

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('fname','lname','username','email', 'password','zipcode','phone')}),
        
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'username', 'fname', 'lname')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email','username',)
    ordering = ('email','username',)
    filter_horizontal = ('groups', 'user_permissions',)



admin.site.register(myModels)#,UserAdmin)
#admin.site.register(Finance)

#admin.site.register(Loan, User_has_Loan, Bank_offers_Loan) 

# Register your models here.
