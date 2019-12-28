from django.db import models
class Subject(models.Model):
    name = models.CharField(max_length=255, null=False);
    code = models.CharField(max_length=255, unique=True, )
