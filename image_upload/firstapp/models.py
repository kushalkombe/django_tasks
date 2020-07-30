from django.db import models

# Create your models here.
class Summer(models.Model):
    imagename=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images/')
    summery=models.CharField(max_length=30)

    def __str__(self):
        return self.imagename
    