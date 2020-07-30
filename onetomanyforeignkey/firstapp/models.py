from django.db import models

# Create your models here.
from django.shortcuts import render
from django.db import models

# Car model uses OneToOneField(Engine)
# Car2 model uses ForeignKey(Engine2, unique=True)

class Engine(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=25)
    engine = models.OneToOneField(Engine,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Engine2(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Car2(models.Model):
    name = models.CharField(max_length=25)
    engine = models.ForeignKey(Engine2, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



