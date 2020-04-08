from django.db import models

# Create your models here.

class Lawnmower(models.Model):
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    photo_url = models.TextField()
    
    def __str__(self):
        return self.model

class Fertilizer(models.Model):
    lawnmower= models.ForeignKey(Lawnmower, on_delete=models.CASCADE, related_name='fertilizers')
    product = models.CharField(max_length=100, default='which product')
    description = models.CharField(max_length=100, default='product description')
    preview_url = models.TextField()

    def __str__(self):
        return self.product