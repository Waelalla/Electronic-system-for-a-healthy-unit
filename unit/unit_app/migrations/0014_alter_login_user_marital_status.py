# Generated by Django 4.1.6 on 2023-03-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_app', '0013_alter_login_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login_user',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('اعزب', 'اعزب'), ('متزوج', 'متزوج'), ('مطلق', 'مطلق'), ('ارمل', 'ارمل')], max_length=20, null=True),
        ),
    ]