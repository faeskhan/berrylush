from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    PRODUCT_CHOICES = (
        ('strawberries', 'Strawberries'),
        ('blueberries', 'Blueberries'),
        ('raspberries', 'Raspberries'),
        ('blackberries', 'Blackberries'),
        ('cherries', 'Cherries'),
        ('jam', 'Jam'),
        ('farm visit', 'Farm Visit'),
    )

    RATING_CHOICES = (
        ('1 star', '1 Star'),
        ('2 stars', '2 Stars'),
        ('3 stars', '3 Stars'),
        ('4 stars', '4 Stars'),
        ('5 stars', '5 Stars'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True, editable = False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    product = models.CharField(max_length=15, choices=PRODUCT_CHOICES, default='farm visit')
    rating = models.CharField(max_length=15, choices=RATING_CHOICES, default='5 stars')
    comment = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Product(models.Model): 
    PRODUCT_CATEGORIES = (
        ('Jam', 'JAM'),
        ('Berries', 'BERRIES'),
        ('Experiences', 'EXPERIENCES'),
    )

    title = models.CharField(max_length=256, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    bio = models.TextField(max_length=256, blank=True, null=True)
    price = models.IntegerField(blank=True, null = True)
    category = models.CharField(max_length=256, choices = PRODUCT_CATEGORIES, blank=True, null=True)

    def __str__(self):
     return self.title