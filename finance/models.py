from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)

