from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Emergencies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100,blank=True)
    emergency = models.CharField(blank=True,max_length=100)
    index = models.IntegerField(default=0)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)
    