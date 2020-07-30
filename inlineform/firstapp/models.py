from django.db import models

# Create your models here.
class Language(models.Model):
    lname=models.CharField(max_length=30)
    def __str__(self):
        return self.lname
class Framework(models.Model):
    fname = models.CharField(max_length=30)
    language=models.ForeignKey(Language,on_delete=models.CASCADE)

    def __str__(self):
        return self.fname
