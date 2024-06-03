from django.db import models

# Create your models here.
class admission(models.Model):
    name = models.CharField(max_length=20, default="")
    contact = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=20, default="")
    Password = models.CharField(max_length=50, default="")
    pass01 = models.CharField(max_length=50, default="")

class feedbackform(models.Model):
    fname = models.CharField(max_length=20, default="")
    lname = models.CharField(max_length=20, default="")
    contact = models.CharField(max_length=50, default="")
    subject = models.CharField(max_length=50, default="")

class admission2(models.Model):
    name = models.CharField(max_length=20, default="")
    contact = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=20, default="")
    Psw = models.CharField(max_length=50, default="")
    psw2 = models.CharField(max_length=50, default="")
