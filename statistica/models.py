from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Variables(models.Model):
    id = models.IntegerField(primary_key=True)
    alias = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    
    
class Charts(models.Model):
    id = models.IntegerField(primary_key=True)
    alias = models.CharField(max_length=255)
    name = models.CharField(max_length=255)