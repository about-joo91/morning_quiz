from mimetypes import init
from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = 'category'
    
    name = models.CharField(max_length=16)
    desc = models.CharField(max_length=128)

class Article(models.Model):
    class Meta:
        db_table = 'article'
    
    title = models.CharField(max_length=16)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)
    