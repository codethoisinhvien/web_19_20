from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()
    max_student = models.IntegerField()
