import os
from datetime import datetime
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

JobTYpe = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)


def job_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join(
        'jobs','images',filename
    )


def job_cv_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join(
        'jobs','resumes',filename
    )


class Job(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15,choices=JobTYpe, default='Full Time')
    description = models.TextField(max_length=5000)
    vacancy = models.IntegerField(default=1)
    #location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    experience = models.IntegerField(default=1) 
    category = models.ForeignKey(to='Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=job_image_upload_to, default='default.png')
    
    published_on = models.DateTimeField(auto_now=True)
 
    slug = models.SlugField(blank=True , null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Application(models.Model):
    job = models.ForeignKey(to=Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to=job_cv_upload_to,default='default_resume.pdf')
    cover_letter = models.TextField(blank=True, null=True)
    applied_on = models.DateTimeField(auto_now=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.job.title}"