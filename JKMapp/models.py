from django.db import models
from django.contrib.auth.models import AbstractUser, User
#from __future__ import unicode_literals


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length = 30)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
    age = models.IntegerField()


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = "student"


class PersonalDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)  # Allow blank
    last_name = models.CharField(max_length=100, blank=True)   # Allow blank
    email = models.EmailField(blank=True)  # Allow blank
    phone_number = models.CharField(max_length=15, blank=True)  # Allow blank

    def __str__(self):
        return self.user.username