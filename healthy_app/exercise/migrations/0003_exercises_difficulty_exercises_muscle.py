# Generated by Django 5.0.3 on 2024-07-05 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_remove_exercises_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercises',
            name='difficulty',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='exercises',
            name='muscle',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
