from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title=models.TextField()
    slug=models.SlugField(unique=True)
    content=models.TextField(null=True,blank=True)



class Blog:
    title="hello"
    content="something.."
    text="new changes"