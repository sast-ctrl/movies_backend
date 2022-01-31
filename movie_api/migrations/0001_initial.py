# Generated by Django 4.0.1 on 2022-01-31 04:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField(default=datetime.datetime.now)),
                ('genre', models.CharField(max_length=50)),
                ('plot', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True)),
            ],
            options={
                'ordering': ('-release_date',),
            },
        ),
    ]
