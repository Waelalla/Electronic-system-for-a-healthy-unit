# Generated by Django 4.2 on 2023-04-27 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_app', '0021_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='home_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_Services', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='services_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_adress', models.CharField(max_length=50)),
                ('imag', models.ImageField(blank=True, null=True, upload_to='department')),
                ('subjact', models.TextField(blank=True, null=True)),
                ('dep_name', models.CharField(max_length=50)),
                ('dep_imag', models.ImageField(blank=True, null=True, upload_to='department')),
                ('Thread_header', models.TextField(blank=True, null=True)),
                ('the_topic', models.TextField(blank=True, null=True)),
                ('the_topic_imag', models.ImageField(blank=True, null=True, upload_to='department')),
                ('Thread_header2', models.TextField(blank=True, null=True)),
                ('the_topic2', models.TextField(blank=True, null=True)),
                ('the_topic_imag2', models.ImageField(blank=True, null=True, upload_to='department')),
                ('Thread_header3', models.TextField(blank=True, null=True)),
                ('the_topic3', models.TextField(blank=True, null=True)),
                ('the_topic_imag3', models.ImageField(blank=True, null=True, upload_to='department')),
                ('Thread_header4', models.TextField(blank=True, null=True)),
                ('the_topic4', models.TextField(blank=True, null=True)),
                ('the_topic_imag4', models.ImageField(blank=True, null=True, upload_to='department')),
                ('Thread_header5', models.TextField(blank=True, null=True)),
                ('the_topic5', models.TextField(blank=True, null=True)),
                ('the_topic_imag5', models.ImageField(blank=True, null=True, upload_to='department')),
            ],
        ),
    ]
