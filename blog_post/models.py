from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
