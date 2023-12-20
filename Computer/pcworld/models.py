from django.db import models
from django.urls import reverse

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, null=True)
    message = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.first_name

class Product(models.Model):
    img = models.ImageField(upload_to='product_img')
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    fulldesc = models.TextField(blank=True)
    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    
    def get_absolute_url(self):
        return reverse("product", kwargs={"product_slug": self.slug})
    
class Component(models.Model):
    img = models.ImageField(upload_to='component_img')
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    fulldesc = models.TextField(blank=True)
    slug = models.SlugField(max_length=128, blank=True, db_index=True, default='')
    
    def get_absolute_url(self):
        return reverse("component", kwargs={"component_slug": self.slug})
    
    
    