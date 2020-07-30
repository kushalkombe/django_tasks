from django.db import models
from django.urls import reverse


# Create your models here.
class Course(models.Model):
    cname=models.CharField(max_length=10)
    duration=models.CharField(max_length=10)
    fees=models.FloatField()

    def __str__(self):
        return self.cname
    def get_absolute_url(self):
        return reverse('course')

class Faculty(models.Model):
    fname=models.CharField(max_length=10)
    fnumber=models.IntegerField()
    fmail=models.EmailField()
    fcourse=models.ManyToManyField(Course)

    def __str__(self):
        return self.fname
    def get_absolute_url(self):
        return reverse('faculty')


class Batch(models.Model):
    bno=models.IntegerField()
    max_strength=models.IntegerField(default=20)
    available_strength=models.IntegerField()
    date_from=models.DateTimeField(null=True)
    bcourse=models.ManyToManyField(Course)

    def __str__(self):
        return str(self.bno)
    def get_absolute_url(self):
        return reverse('batch')


class Student(models.Model):
    suname=models.CharField(max_length=10, unique=True)
    sname=models.CharField(max_length=10)
    spassword=models.CharField(max_length=10)
    saddress=models.CharField(max_length=10)
    semail=models.EmailField()
    snumber=models.IntegerField()
    sbatch=models.ForeignKey(Batch, on_delete=models.CASCADE)

    def __str__(self):
        return self.suname
    def get_absolute_url(self):
        return reverse('login')

class Studymaterial(models.Model):
    slug = models.SlugField(verbose_name='slug')
    file = models.FileField(verbose_name='file', upload_to='document')
    mcourse=models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.slug)
