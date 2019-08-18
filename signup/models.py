from django.db import models

# Create your models here.
class UserDetails(models.Model):
    uname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    pswd = models.CharField(max_length=50)
    rpswd = models.CharField(max_length=50)

class login(models.Model):
    uname=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    
