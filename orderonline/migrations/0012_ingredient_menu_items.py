# Generated by Django 3.2.23 on 2024-02-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderonline', '0011_auto_20240219_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='menu_items',
            field=models.ManyToManyField(blank=True, through='orderonline.MenuItemIngredient', to='orderonline.MenuItem'),
        ),
    ]
