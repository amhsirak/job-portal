from django.db import models
from datetime import datetime
from jobs.models import Job

class Application(models.Model):
  
  job = models.CharField(max_length=100)
  job_id = models.IntegerField()
  creator = models.CharField(max_length=200)
  creator_id = models.IntegerField()
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  resume = models.FileField(upload_to='doc', blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  # Main field to be displayed 
  def __str__(self):
    return self.name