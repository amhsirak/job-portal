from django.db import models
from datetime import datetime

class Contact(models.Model):
  name = models.CharField(max_length=200)
  company = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=11)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)


  def __str__(self):
    return self.name
