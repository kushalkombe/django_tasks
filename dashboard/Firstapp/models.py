from django.db import models
from Userapp.models import UserReg
# Create your models here.

class Address(models.Model):
    city=models.CharField(max_length=30)

    def __str__(self):
        return self.city

class ITJobs(models.Model):
    job_company=models.CharField(max_length=30)
    job_title=models.CharField(max_length=30)
    job_description=models.TextField()
    job_designation=models.CharField(max_length=30)
    job_experience=models.FloatField()
    job_package=models.FloatField()
    job_positionn=models.IntegerField() #no of post available
    job_date_from=models.DateField()
    job_date_to=models.DateField()
    job_location=models.ForeignKey(Address,on_delete=models.CASCADE)
    user_it=models.ManyToManyField(UserReg,default=False)

    def __str__(self):
        return self.job_company

class MECHJobs(models.Model):
    job_company=models.CharField(max_length=30)
    job_title=models.CharField(max_length=30)
    job_description=models.TextField()
    job_designation=models.CharField(max_length=30)
    job_experience=models.FloatField()
    job_package=models.FloatField()
    job_position=models.IntegerField() #no of post available
    job_date_from=models.DateField()
    job_date_to=models.DateField()
    job_location=models.ForeignKey(Address,on_delete=models.CASCADE)
    user_mech=models.ManyToManyField(UserReg,default=False)


    def __str__(self):
        return self.job_company

class CIVILJobs(models.Model):
    job_company=models.CharField(max_length=30)
    job_title=models.CharField(max_length=30)
    job_description=models.TextField()
    job_designation=models.CharField(max_length=30)
    job_experience=models.FloatField()
    job_package=models.FloatField()
    job_position=models.IntegerField() #no of post available
    job_date_from=models.DateField()
    job_date_to=models.DateField()
    job_location=models.ForeignKey(Address,on_delete=models.CASCADE)
    user_civil=models.ManyToManyField(UserReg,default=False)

    def __str__(self):
        return self.job_company




# from django.contrib.auth.models import BaseUserManager
'''

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


from django.contrib.auth.models import AbstractUser, BaseUserManager ## A new class is imported. ##
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# class User(AbstractUser):
#     """User model."""

#     ## Here goes the model definition from before. ##

#     objects = UserManager() ## This is the new line in the User model. ##
'''