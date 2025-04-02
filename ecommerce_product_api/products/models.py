from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    created_date  = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image_url  = models.ImageField(upload_to='products', blank=True, null=True)
    # available = models.BooleanField(default=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('products:product_detail', kwargs={'id':self.id, 'slug':self.slug})
    