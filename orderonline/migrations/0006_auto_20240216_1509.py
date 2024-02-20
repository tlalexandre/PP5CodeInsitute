# Generated by Django 3.2.23 on 2024-02-16 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderonline', '0005_auto_20240216_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderonline.menuitem')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='option',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orderonline.ingredientoption'),
        ),
    ]
