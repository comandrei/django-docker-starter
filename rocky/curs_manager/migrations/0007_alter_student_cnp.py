# Generated by Django 4.1.4 on 2023-01-17 18:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curs_manager', '0006_alter_student_cnp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cnp',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(13)]),
        ),
    ]
