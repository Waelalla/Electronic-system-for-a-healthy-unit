# Generated by Django 4.1.7 on 2023-06-07 14:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logina', '0027_hild_delete_child'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='hild',
            new_name='Child',
        ),
    ]
