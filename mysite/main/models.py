from django.db import models
from django.db.models.fields import CharField





class Role(models.Model):
    #software engineer, software developer, web developer, etc.
    role = models.CharField(max_length=50)
    def __str__(self):
        return self.role

class Level(models.Model):
    #intern, entry, seior, etc.
    level = models.CharField(max_length=20)
    def __str__(self):
        return self.level

class Status(models.Model):
    #in progress, declined, offered
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.status


class Application(models.Model):
    #could set up a separate table for company
    company = models.CharField(max_length=50)
    role = models.ForeignKey(Role, default=1, verbose_name="Role", on_delete=models.SET_DEFAULT)
    pay = models.CharField(max_length=30, default="N/A")
    benefits = models.TextField(default="N/A")
    location = models.CharField(max_length=50)
    notes = models.TextField(default="N/A")
    level = models.ForeignKey(Level, default=1, verbose_name="Level", on_delete=models.SET_DEFAULT)
    status = models.ForeignKey(Status, default=1, verbose_name="Status", on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.company
# Create your models here.
