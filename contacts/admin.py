from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'email', 'car_title', 'city', 'create_date')
    list_display_links = ('user_id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'car_title')
    list_per_page = 25

# Register your models here.
admin.site.register(Contact, ContactAdmin)


