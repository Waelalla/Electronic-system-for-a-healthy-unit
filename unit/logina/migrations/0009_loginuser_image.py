# Generated by Django 4.2 on 2023-04-18 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logina', '0008_alter_loginuser_nationalid'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginuser',
            name='image',
            field=models.ImageField(blank=True, default='photos/default.png', null=True, upload_to='photos'),
        ),
    ]
