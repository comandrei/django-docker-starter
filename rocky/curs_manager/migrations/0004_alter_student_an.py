# Generated by Django 4.1.4 on 2023-01-17 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curs_manager', '0003_alter_student_telefon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='an',
            field=models.IntegerField(db_index=True, default=1),
        ),
    ]
