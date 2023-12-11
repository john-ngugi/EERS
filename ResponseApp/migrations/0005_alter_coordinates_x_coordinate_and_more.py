# Generated by Django 5.0 on 2023-12-10 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResponseApp', '0004_fireresources_location_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinates',
            name='x_coordinate',
            field=models.DecimalField(decimal_places=7, max_digits=8),
        ),
        migrations.AlterField(
            model_name='coordinates',
            name='y_coordinate',
            field=models.DecimalField(decimal_places=7, max_digits=8),
        ),
    ]
