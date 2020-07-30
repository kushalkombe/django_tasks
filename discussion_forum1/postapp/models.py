from django.db import models
from userapp.models import User

# Create your models here.
class Post(models.Model):
    title=models.TextField()
    description=models.TextField()
    ptag=models.TextField()
    fileupload=models.FileField(upload_to='FileUpload/',null='' ,blank=True)
    postbyuser=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


