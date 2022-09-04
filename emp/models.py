from django.db import models


class Employee(models.Model):
    Empnum = models.IntegerField()
    Empname = models.CharField(max_length=20)
    salary = models.IntegerField()
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.Empname
# Create your models here.
