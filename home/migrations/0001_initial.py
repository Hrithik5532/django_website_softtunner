# Generated by Django 3.2.6 on 2021-11-28 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='upload/')),
                ('Post_date', models.DateTimeField(default=datetime.datetime(2021, 11, 28, 19, 56, 32, 810549))),
                ('writer_name', models.CharField(default='', max_length=20)),
                ('heading', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50, null=True)),
                ('blog_link', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('time', models.CharField(max_length=20)),
                ('file', models.ImageField(blank=True, upload_to='upload/contact_files/')),
                ('service', models.CharField(max_length=32)),
                ('budget', models.CharField(max_length=32)),
                ('message', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpic', models.ImageField(upload_to='upload/')),
                ('descrip', models.CharField(max_length=100)),
            ],
        ),
    ]
