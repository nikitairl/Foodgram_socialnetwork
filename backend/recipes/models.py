from colorfield.fields import ColorField
from django.core.validators import MinValueValidator
from django.db import models

from users.models import User


class Ingredient(models.Model):
    ingredientname = models.CharField(
        max_length=150,
        verbose_name='Ингридиент',
        help_text='Используемый при приготовлении ингридиент',
    )
    amount = models.CharField(
        max_length=200,
        verbose_name='Количество',
        help_text='Количество ингридиента',
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'


class Tag(models.Model):
    tagname = models.CharField(
        max_length=150,
        verbose_name='Тег',
        help_text='Название тега',
    )
    slug = models.SlugField(
        unique=True,
        max_length=150,
        verbose_name='Адрес тега',
        help_text='Адрес тега',
    )
    color = ColorField(
        format='hex',
        verbose_name='Цвет',
        help_text='Выбирайте цвет',
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.slug


class Recipe(models.Model):
    recipename = models.CharField(
        max_length=200,
        verbose_name='Название',
        help_text='Введите название рецепта',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
        help_text='Автор рецепта',
    )
    text = models.TextField(
        max_length=1000,
        verbose_name='Описание',
        help_text='Описание рецепта',
    )
    time = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Время приготовления',
    )
    image = models.ImageField(
        upload_to='recipes/image',
        help_text='Загрузите лучшее изображение вашего блюда',
    )
    tags = models.ManyToManyField(
        Tag,
        through='TagRecipe',
        verbose_name='Тег рецепта',
        help_text='Выберите тег рецепта')
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientRecipe',
        related_name='recipes',
        verbose_name='Продукты в рецепте',
        help_text='Выберите продукты рецепта')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Добавить дату создания')

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.recipename


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
        help_text='Пользователь - подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
        help_text='Автор - тот на кого осуществляется подписка'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(fields=['user', 'following'],
                                    name='unique_subscribe')
        ]

    def __str__(self):
        return f'{self.user} {self.following}'


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        help_text='Выберите пользователя'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='carts',
        verbose_name='Рецепты',
        help_text='Рецепт для корзины'
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины пользователей'
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique_cart')
        ]

    def __str__(self):
        return f'{self.user} {self.recipe}'


class IngredientRecipe(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredientrecipes',
        verbose_name='Список продуктов',
        help_text='Добавить продукты')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredientrecipes',
        verbose_name='Рецепт',
        help_text='Выберите рецепт'
    )
    amount = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name='Количество',
        help_text='Нужное количество'
    )

    class Meta:
        verbose_name = 'Продукты согласно рецепту'
        verbose_name_plural = 'Продукты согласно рецепту'
        constraints = [
            models.UniqueConstraint(fields=['ingredient', 'recipe'],
                                    name='unique_ingredientrecipe')
        ]

    def __str__(self):
        return f'{self.ingredient} {self.recipe}'


class TagRecipe(models.Model):
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name='Теги',
        help_text='Выберите теги рецепта'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        help_text='Выберите рецепт')

    class Meta:
        verbose_name = 'Теги рецепта'
        verbose_name_plural = 'Теги рецепта'
        constraints = [
            models.UniqueConstraint(fields=['tag', 'recipe'],
                                    name='unique_tagrecipe')
        ]

    def __str__(self):
        return f'{self.tag} {self.recipe}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        help_text='Избранный пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт',
        help_text='Выберите рецепт'
    )

    class Meta:
        verbose_name = 'Избранный'
        verbose_name_plural = 'Избранные'
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique_favorite')
        ]

    def __str__(self):
        return f'{self.recipe} {self.user}'
