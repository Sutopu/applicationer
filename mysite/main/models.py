from django.db import models
from django.db.models.fields import CharField



class Application(models.Model):
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    pay = models.CharField(max_length=30)
    benefits = models.TextField()
    location = models.CharField(max_length=50)
    notes = models.TextField()
    status = models.CharField(max_length=10)
# Create your models here.
