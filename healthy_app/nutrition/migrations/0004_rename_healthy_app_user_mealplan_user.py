# Generated by Django 5.0.3 on 2024-06-08 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0003_alter_mealplan_healthy_app_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mealplan',
            old_name='healthy_app_user',
            new_name='user',
        ),
    ]
