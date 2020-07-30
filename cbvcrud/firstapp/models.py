from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=20)
    srollno=models.IntegerField()
    saddr=models.CharField(max_length=20)
    
