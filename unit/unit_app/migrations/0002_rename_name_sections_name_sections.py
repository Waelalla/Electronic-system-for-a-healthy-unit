# Generated by Django 4.1.6 on 2023-02-27 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sections',
            old_name='name',
            new_name='name_sections',
        ),
    ]
