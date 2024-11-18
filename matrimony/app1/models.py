from django.db import models

# Create your models here.

class Basicdetails(models.Model):
    age=models.IntegerField()
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    email=models.EmailField(max_length=40)