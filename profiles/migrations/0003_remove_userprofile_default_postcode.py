# Generated by Django 3.2.23 on 2024-03-19 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20240319_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_postcode',
        ),
    ]
