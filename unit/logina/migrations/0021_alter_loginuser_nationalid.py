# Generated by Django 4.1 on 2023-05-04 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logina', '0020_remove_profile_user_alter_loginuser_nationalid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='NationalId',
            field=models.CharField(max_length=200),
        ),
    ]
