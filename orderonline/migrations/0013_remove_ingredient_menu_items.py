# Generated by Django 3.2.23 on 2024-02-19 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderonline', '0012_ingredient_menu_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='menu_items',
        ),
    ]
