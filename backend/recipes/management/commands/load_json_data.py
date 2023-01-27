import json
from django.core.management.base import BaseCommand

from recipes.models import Ingredient
"""
Импорт базы данных json в django проект
"""


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data/ingredients.json', 'rb') as f:
            data = json.load(f)
            for i in data:
                ingredient = Ingredient()
                ingredient.ingredientname = i['name']
                ingredient.amount = i['measurement_unit']
                ingredient.save()
                print(i['name'], i['measurement_unit'])
