from django.db import models

# Create your models here.
class Patient(models.Model):
    names = models.CharField(max_length=100)
    dr = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    test = models.CharField(max_length=100)
    result = models.CharField(max_length=150)
    
