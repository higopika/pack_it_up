from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class flightInfo(models.Model):
    flightName = models.CharField(max_length=50)
    date = models.DateField()
    noOfSeats = models.IntegerField()
    duration = models.TimeField()
    stop = models.BooleanField()
    price = models.FloatField()

