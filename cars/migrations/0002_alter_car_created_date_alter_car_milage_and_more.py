# Generated by Django 4.2.2 on 2023-07-06 07:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 6, 12, 55, 19, 604734)),
        ),
        migrations.AlterField(
            model_name='car',
            name='milage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='passengers',
            field=models.IntegerField(),
        ),
    ]