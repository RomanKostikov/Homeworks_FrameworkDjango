# Generated by Django 5.0.1 on 2024-01-21 14:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
