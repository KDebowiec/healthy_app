# Generated by Django 5.0.3 on 2024-04-22 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercises',
            name='email',
        ),
    ]
