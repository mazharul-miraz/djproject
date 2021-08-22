from django.db import models
from django.db.models.base import Model

# Create your models here.

class Artical(models.Model):
    
    title       = models.CharField(max_length=120)
    content     = models.TextField()
    active      = models.BooleanField(default=True)

