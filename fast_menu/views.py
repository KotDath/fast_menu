from django.http import HttpResponse
from django.template import loader
from .models import Dish, Category, Config


def main(request):
    template = loader.get_template('fast_menu/index.html')
    categories = Category.objects.all()
    config = Config.objects.all().first()
    groups = {}
    for category in categories:
        dishes = Dish.objects.filter(item_category=category)
        if len(dishes) > 0:
            groups[category.category_name] = dishes
    context = {
        "title": 'Краснодар',
        "page_name": 'Dish Menu bar',
        "groups": groups,
        "config": config,
    }
    return HttpResponse(template.render(context, request))
