from django.contrib import admin

from users.models import User
from .models import (Cart, Favorite, Ingredient, IngredientRecipe, Recipe,
                     Subscribe, Tag, TagRecipe)


class TagRecipeInline(admin.TabularInline):
    """
    Настройка тегов в админке
    """
    model = TagRecipe
    extra = 0


class SubscribeAdmin(admin.ModelAdmin):
    """
    Параметры админ зоны.
    """
    list_display = ('user', 'following')
    search_fields = ('user', )
    empty_value_display = '-пусто-'
    list_filter = ('user',)


class IngredientRecipeInline(admin.TabularInline):
    """
    Настройка модели ингридиентов в админке
    """
    model = IngredientRecipe
    extra = 0


class UserAdmin(admin.ModelAdmin):
    """
    Параметры админ зоны пользователя.
    """
    list_display = ('username', 'email', 'id')
    search_fields = ('username', 'email')
    empty_value_display = '-пусто-'
    list_filter = ('username', 'email')


class IngredientAdmin(admin.ModelAdmin):
    """
    Параметры админ зоны продуктов.
    """
    list_display = ('ingredientname', 'amount')
    search_fields = ('ingredientname', )
    verbose_name = 'Ингридиент'
    empty_value_display = '-пусто-'
    list_filter = ('ingredientname',)


class TagAdmin(admin.ModelAdmin):
    """
    Параметры админ зоны тэгов.
    """
    list_display = ('tagname', 'color', 'slug')
    search_fields = ('tagname', )
    empty_value_display = '-пусто-'
    list_filter = ('tagname',)


class CartAdmin(admin.ModelAdmin):
    """
    Параметры админ зоны продуктовой корзины.
    """
    list_display = ('user', 'recipe', 'id')
    search_fields = ('user', )
    empty_value_display = '-пусто-'
    list_filter = ('user',)


class FavoriteAdmin(admin.ModelAdmin):
    """
    Параметры админ зоны избранных рецептов.
    """
    list_display = ('user', 'recipe')
    search_fields = ('user', )
    empty_value_display = '-пусто-'
    list_filter = ('user',)


class RecipeAdmin(admin.ModelAdmin):
    """
    Параметры админ зоны рецептов.
    """

    inlines = (IngredientRecipeInline, TagRecipeInline,)
    list_display = ('recipename', 'author', 'time',
                    'id', 'count_favorite', 'pub_date')
    search_fields = ('recipename', 'author', 'tags')
    empty_value_display = '-пусто-'
    list_filter = ('recipename', 'author', 'tags')

    def count_favorite(self, obj):
        return Favorite.objects.filter(recipe=obj).count()
    count_favorite.short_description = 'В избранном столько раз'


admin.site.register(Cart, CartAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Recipe, RecipeAdmin)
