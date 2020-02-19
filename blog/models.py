from django.db import models

# Create your models here.
# create a blog models, ex:
    # title
    # pub_date
    # body
    # image

class Blog(models.Model):
    title = models.CharField(max_length=225)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')