from django.db import models
import uuid
# Create your models here.


class FireResources(models.Model):
    fire = models.IntegerField(default=34)
    location_name = models.CharField(max_length=50,null=True)
    rfid =  models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    
    def __str__(self):
        return str(self.rfid)

class MedicalResourses(models.Model):
    medical = models.IntegerField(default=34)
    location_name = models.CharField(max_length=50,null=True)
    rfid =  models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    
    def __str__(self):
        return str(self.rfid)
    

class PoliceResources(models.Model):
    police = models.IntegerField(default=34)
    location_name = models.CharField(max_length=50,null=True)
    rfid =  models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    def __str__(self):
        return str(self.rfid)
    
class Coordinates(models.Model):
    x_coordinate =  models.CharField(max_length=50,null=True)
    y_coordinate =  models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

