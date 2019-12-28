from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    role = models.IntegerField(default=1)
