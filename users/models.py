from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(primary_key=True)
    role = models.IntegerField()
    password = models.CharField(max_length=128)
