# Generated by Django 5.1.6 on 2025-03-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foodproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='price',
            field=models.IntegerField(default=100),
        ),
    ]
