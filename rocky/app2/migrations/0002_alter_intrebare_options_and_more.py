# Generated by Django 4.1.4 on 2023-02-09 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='intrebare',
            options={'verbose_name_plural': 'Intrebari'},
        ),
        migrations.AlterModelOptions(
            name='variantaraspuns',
            options={'verbose_name_plural': 'Variante Raspuns'},
        ),
    ]