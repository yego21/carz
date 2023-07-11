from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    
    def thumbnail(self, object):
        return format_html("<img src='{}' width='40px' style='border-radius: 50%'>".format(object.photo.url))
    
    # fieldsets = [
    #     (None, {"fields": ["question_text"]}),
    #     ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    # ]
    
    list_display_links = (Team.__str__,)
    
    thumbnail.short_description = 'Photo'
    
    list_display = ["id", "thumbnail", Team.__str__, "designation"]
    
    list_filter = ["designation"]
    
    search_fields = ["first_name", "designation"]
    
admin.site.register(Team, TeamAdmin)
