# Generated by Django 4.1.4 on 2023-02-07 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curs_manager', '0016_alter_student_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adresa',
            options={'verbose_name_plural': 'adrese'},
        ),
        migrations.AlterModelOptions(
            name='adresanoua',
            options={'verbose_name_plural': 'Adrese Noi'},
        ),
        migrations.AlterModelOptions(
            name='curs',
            options={'verbose_name_plural': 'cursuri'},
        ),
    ]
