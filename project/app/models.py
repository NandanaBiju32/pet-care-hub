from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')

# class Pet(models.Model):
#         pet_type = models.CharField(max_length=100)
#         breed = models.CharField(max_length=100)
#         name = models.CharField(max_length=100)
#         age = models.CharField(max_length=50)
#         weight = models.CharField(max_length=50)
#         owner_name = models.CharField(max_length=100)
#         contact = models.CharField(max_length=15)
#         image = models.URLField()
#         place = models.CharField(max_length=100)
#
#         def __str__(self):
#             return self.name


class Pet(models.Model):

    pet_type = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    # image = models.URLField()
    image = models.ImageField(upload_to='pets/')

# Create your models here.
