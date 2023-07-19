from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    
    def thumbnail(self, object):
        return format_html("<img src='{}' width='40px' style='border-radius: 50%'>".format(object.car_photo.url))
    
    # fieldsets = [
    #     (None, {"fields": ["question_text"]}),
    #     ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    # ]
    
    list_display_links = ("thumbnail", "car_title")
    
    thumbnail.short_description = ''
    
    list_display = ["id", "thumbnail", "car_title", "city", "model", "transmission", "body_style", "is_featured"]
    
    list_filter = ["model", "city", "body_style"]
    
    search_fields = ["model", "city", "body_style"]
    
    list_editable = ["is_featured"]
    
admin.site.register(Car, CarAdmin)
    
    
    
