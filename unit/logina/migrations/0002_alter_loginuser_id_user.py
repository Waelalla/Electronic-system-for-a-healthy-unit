# Generated by Django 4.2 on 2023-04-15 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='id_user',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
