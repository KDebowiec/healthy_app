# Generated by Django 5.0.3 on 2024-06-08 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0003_alter_mealplan_healthy_app_user'),
        ('users', '0003_remove_healthyappuser_user_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HealthyAppUser',
        ),
    ]
