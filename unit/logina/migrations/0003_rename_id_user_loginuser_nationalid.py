# Generated by Django 4.2 on 2023-04-15 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logina', '0002_alter_loginuser_id_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginuser',
            old_name='id_user',
            new_name='NationalId',
        ),
    ]
