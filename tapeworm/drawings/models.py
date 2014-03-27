from django.db import models
from django.contrib.auth.models import User

from jsonfield import JSONField

# Create your models here.

class Drawing(models.Model):
  owner = models.ForeignKey(User)
  title = models.CharField(max_length=200)
  json = JSONField()

  def __unicode__(self):
    return self.title
