from django.contrib import admin

from .models import Dish, Category, Config

admin.site.register(Dish)
admin.site.register(Category)
admin.site.register(Config)
