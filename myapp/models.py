from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField()
    price = models.DecimalField(max_digits=100000 ,decimal_places=2)

class Review(models.Model):
    # product = models.ForeignKey()
    author = models.CharField(max_length=400)
    text_review = models.TextField()
    rating = models.IntegerField()