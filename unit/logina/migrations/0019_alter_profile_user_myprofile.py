# Generated by Django 4.2 on 2023-04-26 03:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.genrate_code


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logina', '0018_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='o', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='myProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='users')),
                ('code', models.CharField(default=utils.genrate_code.genrate_code, max_length=10)),
                ('code_used', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
