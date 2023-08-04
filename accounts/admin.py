from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# # Register your models here.
# class AccountsAdmin(admin.ModelAdmin):
    
UserAdmin.list_display = ["id", "first_name", "last_name"]


  
    
    
# admin.site.register(User, AccountsAdmin)