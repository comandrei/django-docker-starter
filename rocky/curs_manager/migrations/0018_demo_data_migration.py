# Generated by Django 4.1.4 on 2023-02-21 17:45

from django.db import migrations

def inainte(apps, models):
    print("Inainte")

def inapoi(app, models):
    print("inapoi")

class Migration(migrations.Migration):

    dependencies = [
        ('curs_manager', '0017_alter_adresa_options_alter_adresanoua_options_and_more'),
    ]

    operations = [
        migrations.RunPython(inainte, inapoi)
    ]
