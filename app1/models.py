from multiprocessing.managers import Server

from django.db import models
from datetime import date

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=12)
    email = models.EmailField(max_length=20)
    caseno = models.CharField(max_length=12)
    lawyer = models.CharField(max_length=20,default="Nil")
    case = models.TextField(max_length=50)
    date = models.DateField(default=date.today)

    # def __str__(self):
    #     return self.name,self.caseno,self.case

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name

class Lawyer(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'lawyer'

class Case(models.Model):
    name = models.CharField(max_length=30)
    caseno = models.CharField(max_length=12)
    lawyer = models.CharField(max_length=20, default="Nil")
    case = models.TextField(max_length=50)
    date = models.DateField(default=date.today)
    def __str__(self):
        return self.name,self.lawyer
    class Meta:
        db_table = 'Case'