# Generated by Django 4.0.1 on 2022-01-31 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_api', '0003_watchlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watchlist',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='movies',
            new_name='movie',
        ),
    ]