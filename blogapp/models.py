from django.db import models

# Create your models here.
class Newpost(models.Model):
    Title = models.CharField(max_length =50)
    Description = models.CharField(max_length = 100)
    Image = models.ImageField(upload_to = "upload")
