
from django.db import models

# Create your models here.
class bookingInfo(models.Model):
    fromDest = models.CharField(max_length=50)
    toDest = models.CharField(max_length=50)
    noOfPeople = models.IntegerField()
    flightClass = models.CharField(max_length=50)
    date = models.DateField()