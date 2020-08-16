from django.db import models

# Create your models here.
from taggit.managers import TaggableManager


class Category(models.Model):
    category_title=models.CharField(max_length=30)

    def __str__(self):
        return self.category_title


class Products(models.Model):
    product_name=models.CharField(max_length=30)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    tags = TaggableManager()
    image=models.ImageField(upload_to='./images/',blank=True)
    description=models.TextField()

    def __str__(self):
        return self.product_name
