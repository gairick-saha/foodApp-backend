from django.contrib import admin
from . import models

admin.site.site_header = "foodApp Admin Dashboard"

class FoodAppAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'category', 'price', 'stock')

admin.site.register(models.Menu, FoodAppAdmin)
admin.site.register(models.MenuCard)
