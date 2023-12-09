from django.db import models
import uuid
# Create your models here.


class Resources(models.Model):
    fire = models.IntegerField(default=34)
    medical = models.IntegerField(default=34)
    crime = models.IntegerField(default=34)
    rfid =  models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    
    def __str__(self):
        return self.rfid  
class Coordinates(models.Model):
    x_coordinate = models.DecimalField(max_digits=2,decimal_places=2)
    y_coordinate = models.DecimalField(max_digits=2,decimal_places=2)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

