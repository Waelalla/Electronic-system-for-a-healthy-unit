# Generated by Django 4.2 on 2023-04-27 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit_app', '0027_delete_sss'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='services_detail',
            new_name='services',
        ),
    ]