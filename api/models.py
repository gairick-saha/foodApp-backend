from django.db import models


class MenuCard(models.Model):
    menu_id = models.AutoField
    Menu_Type = models.CharField(max_length=120, db_index=True, default='')
    slug = models.SlugField(max_length=120, db_index=True, default='')
    image = models.ImageField(upload_to='shop/images', blank=True)

    class Meta:
        ordering = ['Menu_Type', ]
        verbose_name = 'Menu Type'
        verbose_name_plural = 'Menu Types'

    def __str__(self):
        return self.Menu_Type

    @property
    def choices(self):
        return self.choice_set.all()


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

    def __str__(self):
        return self.item_name
