# Generated by Django 4.2.2 on 2023-07-11 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='created_date',
            new_name='create_date',
        ),
    ]
