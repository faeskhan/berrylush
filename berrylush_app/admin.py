from django.contrib import admin

# Register your models here.
from .models import Review, Product

admin.site.register(Review)
admin.site.register(Product)