from django.db import models


class Seat(models.Model):
    name = models.CharField(max_length=255)
