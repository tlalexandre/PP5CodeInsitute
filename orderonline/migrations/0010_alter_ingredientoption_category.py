# Generated by Django 3.2.23 on 2024-02-16 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderonline', '0009_alter_ingredientoption_menu_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientoption',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orderonline.menucategory'),
        ),
    ]