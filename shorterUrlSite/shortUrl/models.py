from django.db import models

class Urls(models.Model):
    link = models.CharField(max_length = 3000)
    shortlink = models.CharField(max_length = 3000, default='')


# Create your models here.
