from django.db import models

# Create your models here.
class Bookstore(models.Model):
    title=models.CharField(max_length=100)
    type= models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title
