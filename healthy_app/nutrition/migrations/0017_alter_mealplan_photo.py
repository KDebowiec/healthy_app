# Generated by Django 5.0.3 on 2024-06-15 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0016_alter_mealplan_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealplan',
            name='photo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
