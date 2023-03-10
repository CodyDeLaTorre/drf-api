from django.db import models
from django.contrib.auth import get_user_model


class Wizard(models.Model):
  creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  name = models.CharField(max_length=64)
  source = models.TextField()
  weapon = models.CharField(max_length=64)
  description = models.TextField()

  #on creation
  created_at = models.DateTimeField(auto_now_add=True)
  #on save
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
