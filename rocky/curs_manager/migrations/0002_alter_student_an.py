# Generated by Django 4.1.4 on 2023-01-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curs_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='an',
            field=models.IntegerField(default=1),
        ),
    ]
