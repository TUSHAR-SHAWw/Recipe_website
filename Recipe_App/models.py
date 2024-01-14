from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from .field import compress_data
# Create your models here.
import zlib

class Recipe(models.Model):
   user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
   recipe_name = models.CharField(max_length=100)
   recipe_description = models.TextField()
   image_data = models.BinaryField(null=True, blank=True)

   def save(self, *args, **kwargs):
       if self.image_data is not None:
           self.image_data = compress_data(self.image_data)
       super().save(*args, **kwargs)