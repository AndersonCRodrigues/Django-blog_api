from django.db import models
from category.models import Category
from django.contrib.auth.models import User
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.title
