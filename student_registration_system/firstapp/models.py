from django.db import models

# Create your models here.
class Student(models.Model):
    srollno = models.IntegerField(blank=True,null=True)
    sname = models.CharField(max_length=30,blank=True,null=True)
    smarks = models.FloatField(blank=True,null=True)
    saddr = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.sname
