# Generated by Django 3.2.16 on 2023-01-08 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'Ингридиент', 'verbose_name_plural': 'Ингридиенты'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(help_text='Загрузите лучшее изображение вашего блюда', upload_to='recipes/image'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipename',
            field=models.CharField(help_text='Введите название рецепта', max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='following',
            field=models.ForeignKey(help_text='Автор - тот на кого осуществляется подписка', on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]