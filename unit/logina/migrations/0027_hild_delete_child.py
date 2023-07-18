# Generated by Django 4.1.7 on 2023-06-07 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logina', '0026_child_remove_sons_user_delete_girl_delete_sons'),
    ]

    operations = [
        migrations.CreateModel(
            name='hild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('national_id', models.CharField(max_length=14)),
                ('gender', models.CharField(blank=True, choices=[('male', 'ذكر'), ('female', 'انثى')], max_length=20, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sons_users', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.DeleteModel(
            name='Child',
        ),
    ]
