# Generated by Django 4.1.6 on 2023-03-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_app', '0011_alter_login_user_age_alter_login_user_id_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login_user',
            name='address',
            field=models.CharField(max_length=20),
        ),
    ]
