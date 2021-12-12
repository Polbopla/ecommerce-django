from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH
from django.urls import reverse

from category.models import Category

# Create your models here.


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True
    )
    slug = models.CharField(
        max_length=200,
        unique=True
    )
    description = models.TextField(
        max_length=500,
        blank=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    images = models.ImageField(
        upload_to='photos/products',
        blank=True
    )
    stock = models.IntegerField()
    is_purchasable = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self) -> str:
        return self.name
