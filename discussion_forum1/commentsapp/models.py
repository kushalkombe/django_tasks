from django.db import models
from userapp.models import User
from postapp.models import Post

# Create your models here.
class Comment(models.Model):
    commentbox=models.TextField(blank=True, null='')
    cfileupload=models.FileField(upload_to='FileUpload/',null='' ,blank=True)
    commentforpost=models.ForeignKey(Post,on_delete=models.CASCADE)
    commentbyuser=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.commentbox
