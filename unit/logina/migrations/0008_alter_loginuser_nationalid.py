# Generated by Django 4.2 on 2023-04-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logina', '0007_alter_loginuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='NationalId',
            field=models.CharField(default=int, max_length=200, unique=True),
        ),
    ]
