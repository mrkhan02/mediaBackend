from email.mime import image
from importlib.resources import contents
from pydoc import describe
from pyexpat import model
from django.db import models
from tinymce.models import HTMLField
from .constants import TAGS
#Article table

class Article(models.Model):
    sno=models.AutoField(primary_key=True)
    thumbnail=models.ImageField()
    title=models.CharField(max_length=1000)
    author=models.CharField(max_length=255)
    profile=models.URLField(null=True,blank=True)
    date=models.DateField()
    content=HTMLField()
    summary=models.TextField(default='')
    isActive=models.BooleanField(default=False)
    tag=models.CharField(choices=TAGS,max_length=100,null=True,blank=True)
    isPinned=models.BooleanField(default=False)
    def __str__(self):
        return self.title



#newsletter table
class Newsletter(models.Model):
    sno=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email=models.EmailField()

    def __str__(self):
        return self.email



#gallery table

class Gallery(models.Model):
    sno=models.AutoField(primary_key=True)
    image=models.ImageField()
    click=models.CharField(max_length=255)
    event=models.TextField()

    def __str__(self):
        return self.click

#comments

class Comments(models.Model):
    sno=models.AutoField(primary_key=True)
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    profile=models.TextField(null=True,blank=True)
    message=models.TextField()

    def __str__(self):
        return self.name


#videos

class Videos(models.Model):
    sno=models.AutoField(primary_key=True)
    link=models.URLField()

    def __str__(self) -> str:
        return str(self.link)



    
class Spotlight(models.Model):
    sno=models.AutoField(primary_key=True)
    url=models.URLField()
    title=models.CharField(max_length=1000)
    summary=models.TextField()
    def __str__(self):
        return self.title


