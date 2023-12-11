from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Emergencies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100,blank=True)
    emergency = models.CharField(blank=True,max_length=100)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)

    def __str__(self):
        return self.location

class indexes(models.Model):
    emergency=models.ForeignKey(Emergencies,on_delete= models.CASCADE)   
    index = models.IntegerField(blank=True) 