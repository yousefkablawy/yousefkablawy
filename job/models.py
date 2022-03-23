from distutils.command.upload import upload
from pydoc import describe
from django.db import models
from django.forms import CharField

# Create your models here.
JOB_TYPE = (('part time', 'part time'), ('full time', 'full time'))


class Job(models.Model):
    title = models.CharField(max_length=100)
    describtion = models.TextField()
    published_at = models.DateTimeField(auto_now=True)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to='jobs/')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
