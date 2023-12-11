from django.db import models
import uuid
# Create your models here.

# Define a Django model for Fire Resources
class FireResources(models.Model):
    fire = models.IntegerField(default=34) # Default value for the 'fire' resource
    location_name = models.CharField(max_length=50,null=True)   # Name of the location
    rfid =  models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4,  # Generate a unique identifier using UUID4
         editable = False)     # The identifier should not be editable   
    
    def __str__(self):
        return str(self.rfid)  # String representation for easy identification

# Define a Django model for Medical Resources
class MedicalResourses(models.Model):
    medical = models.IntegerField(default=34)
    location_name = models.CharField(max_length=50,null=True)
    rfid =  models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    
    def __str__(self):
        return str(self.rfid)
    
# Define a Django model for Police Resources
class PoliceResources(models.Model):
    police = models.IntegerField(default=34)
    location_name = models.CharField(max_length=50,null=True)
    rfid =  models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    def __str__(self):
        return str(self.rfid)
# Define a Django model for Coordinates
class Coordinates(models.Model):
    x_coordinate =  models.CharField(max_length=50,null=True)  # X-coordinate value
    y_coordinate =  models.CharField(max_length=50,null=True)  # Y-coordinate value
    name = models.CharField(max_length=100)  # Name for the coordinates

    def __str__(self):
        return self.name
