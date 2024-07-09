from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Livro(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=250)
    slug = models.SlugField()
    cover = models.ImageField(upload_to='bibliotech/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title