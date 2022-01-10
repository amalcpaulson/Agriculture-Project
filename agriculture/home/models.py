from django.db import models

# Create your models here.

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    adr = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    mobile = models.IntegerField
    gender = models.CharField(max_length=6)
    age = models.IntegerField
    occupation = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.first_name} {self.last_name} -> {self.occupation}"