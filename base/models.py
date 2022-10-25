from unittest.util import _MAX_LENGTH
from xml.parsers.expat import model
from django.db import models

class User(models.Model):
    first_name = models.CharField("Primeiro nome", max_length=30)
    second_name = models.CharField("Segundo nome", max_length=30)
    tell = models.CharField(max_length=11)
    email = models.EmailField()


# Create your models here.
