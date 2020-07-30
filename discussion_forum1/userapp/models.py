from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    confirm_password=models.CharField(max_length=30)
    email=models.EmailField()
    gender_male = 0
    gender_female = 1
    gender_choices = [(gender_male, 'Male'), (gender_female, 'Female')]
    gender = models.IntegerField(choices=gender_choices)
    tags=models.TextField()
    def __str__(self):
        return self.name
