from django.db import models

# Create your models here.

class Coordinates(models.Model):
    x_coordinate = models.DecimalField(max_digits=2,decimal_places=2)
    y_coordinate = models.DecimalField(max_digits=2,decimal_places=2)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    