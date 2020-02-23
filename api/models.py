from django.db import models
from djmoney.models.fields import MoneyField


class MenuCard(models.Model):
    menu_id = models.AutoField
    menu_type = models.CharField(max_length=120, db_index=True, default='')
    slug = models.SlugField(max_length=120, db_index=True, default='')
    image = models.ImageField(upload_to='shop/images', blank=True)
    # items = models.CharField(max_length=120, db_index=True, default='')

    class Meta:
        ordering = ['slug', ]
        verbose_name = 'Menu Type'
        verbose_name_plural = 'Menu Types'

    def __str__(self):
        return self.menu_type

class Menu(models.Model):
    category = models.ForeignKey(
        MenuCard, on_delete=models.CASCADE, default=None)
    item_name = models.CharField(max_length=120, db_index=True, verbose_name='items')
    slug = models.SlugField(max_length=120, db_index=True)
    image = models.ImageField(upload_to='shop/images', blank=True)
    description = models.TextField(blank=True)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='INR', default=0)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

    @property
    def category_type(self):
        return self.category
