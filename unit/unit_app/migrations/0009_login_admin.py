# Generated by Django 4.1.6 on 2023-03-01 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_app', '0008_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='login_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]