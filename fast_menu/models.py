from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, help_text='dish category')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Dish(models.Model):
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=50, help_text='dish name')
    item_price = models.IntegerField()
    item_description = models.CharField(max_length=200, help_text='description')

    def __str__(self):
        return self.dish_name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюдо'


class Config(models.Model):
    header_font = models.CharField(max_length=50, help_text='header font')
    group_font = models.CharField(max_length=50, help_text='group font')
    dish_font = models.CharField(max_length=50, help_text='dish font')
    header_color = models.CharField(max_length=50, help_text='header color')
    group_color = models.CharField(max_length=50, help_text='group color')
    dish_color = models.CharField(max_length=50, help_text='dish color')
    header_size = models.IntegerField()
    group_size = models.IntegerField()
    dish_size = models.IntegerField()
