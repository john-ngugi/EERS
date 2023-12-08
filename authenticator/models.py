from django.db import models
from django.contrib.auth.models import User
'''from django.urls import reverse'''

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length= 50)
    
    def __str__(self):
        return self.username + ' | ' + str(self.author)
    
    '''class RegisterForm(models.Model):
        username = models.CharField(max_length=50)
        password = models.CharField(max_length= 50)'''
    
    
    '''def get_absolute_url(self):
        return reverse('home')'''
    
    