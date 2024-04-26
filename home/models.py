from django.db import models

# Create your models here.
class info(models.Model):
    name=models.CharField(max_length=200)
    age=models.PositiveIntegerField()

class info1(models.Model):
    name=models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    father_name=models.CharField(max_length=200)
    father_age=models.PositiveIntegerField()
