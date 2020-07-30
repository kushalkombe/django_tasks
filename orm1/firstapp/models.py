from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Country(models.Model):
    cid=models.AutoField(primary_key=True)
    country_name=models.CharField(max_length=35)
    class Meta:
        db_table='country'
    def __str__(self):
        return f'{self.country_name}'

class Employee(models.Model):
    eid=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=30)
    ecom=models.CharField(max_length=30)
    esal=models.FloatField()
    eaddr=models.ForeignKey(Country,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.ename}'

class Language(models.Model):
    lid=models.AutoField(primary_key=True)
    lname=models.CharField(max_length=30)
    employee=models.ManyToManyField(Employee)
    def __str__(self):
        return f'{self.lname}'
        