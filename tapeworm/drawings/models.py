from django.db import models
from django.contrib.auth import User

from jsonfield import JSONfield

# Create your models here.

class Drawing(models.Model):
  owner = models.ForeignKey(User)
  name = models.CharField()
  json = JSONfield()