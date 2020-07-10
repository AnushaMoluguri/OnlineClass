from django.db import models

class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    Contactno = models.IntegerField(unique=True)
    emailid = models.EmailField(unique=True)
    password= models.CharField(max_length=20)

class AddClassModel(models.Model):
      Name=models.CharField(max_length=20)
      Faculty=models.CharField(max_length=20)
      Date=models.DateField()
      Time=models.TimeField()
      Fee=models.FloatField()
      Duration=models.IntegerField()
