# Generated by Django 4.1.4 on 2023-01-24 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curs_manager', '0015_caine'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('nume', 'prenume', 'an')},
        ),
    ]