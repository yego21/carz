from django.db import models
from django.contrib import admin

# Create your models here.
class Team(models.Model):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%d/%m/%Y')
    designation = models.CharField(max_length=100)
    facebook = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    
    @admin.display(      
      ordering="id",
      description="Name",
    )
    def __str__(self):
        return self.first_name+" "+self.last_name
    
    
    def name(self):
        return self.first_name+" "+self.last_name
    
    
    