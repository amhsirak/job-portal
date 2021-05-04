from django.db import models
from datetime import datetime
from django.conf import settings

CONTRACT = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
    ('Freelance', 'Freelancer'),
)

LOCATION = (
    ('Mumbai','Mumbai'),
    ('Bangalore','Bangalore'),
    ('Pune','Pune'),
    ('Remote','Remote'),
)


class Job(models.Model):

    creator = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.DO_NOTHING) 
    company = models.CharField(max_length=200, default=None)
    title = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(choices=LOCATION,max_length=50)
    description = models.TextField(blank=True)
    about = models.TextField(blank=True)
    job_date = models.DateTimeField(default=datetime.now ,blank = True)
    contract = models.CharField(choices=CONTRACT,max_length=150)
    is_published = models.BooleanField(default=True)
    vacancy = models.CharField(max_length=10, null=True)
    experience = models.CharField(max_length=100)
    salary = models.IntegerField()
    deadline = models.DateTimeField()
    main_image = models.ImageField(upload_to='photos/%Y/%m%d/')

    # Function to return main field which we are considering to be title
    def __str__(self):
        return self.title