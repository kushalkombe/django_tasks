from django.db import models

# Create your models here.
class Pune(models.Model):
    headline=models.CharField(max_length=150)
    newsfield=models.TextField()

class Nagpur(models.Model):
    headline=models.CharField(max_length=150)
    newsfield=models.TextField()

class Mumbai(models.Model):
    headline = models.CharField(max_length=150)
    newsfield = models.TextField()
