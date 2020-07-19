from datetime import datetime

from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50 )


class Blog (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now, blank=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

