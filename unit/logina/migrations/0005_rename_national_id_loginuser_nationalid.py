# Generated by Django 4.2 on 2023-04-15 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logina', '0004_rename_nationalid_loginuser_national_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginuser',
            old_name='National_Id',
            new_name='NationalId',
        ),
    ]