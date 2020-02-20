from django.db import models
from bson.objectid import ObjectId


class MenuCard(models.Model):
    menu_id = models.AutoField
    Menu_Type = models.CharField(max_length=120, db_index=True, default='')
    slug = models.SlugField(max_length=120, db_index=True, default='')

    class Meta:
        ordering = ['Menu_Type', ]
        verbose_name = 'Menu Card'
        verbose_name_plural = 'Menu Cards'

    def __str__(self):
        return self.Menu_Type


class Menu(models.Model):
    category = models.ForeignKey(
        MenuCard, on_delete=models.CASCADE, default=None)
    item_name = models.CharField(max_length=120, db_index=True)
    slug = models.SlugField(max_length=120, db_index=True)
    image = models.ImageField(upload_to='shop/images', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['item_name', ]
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return self.item_name
