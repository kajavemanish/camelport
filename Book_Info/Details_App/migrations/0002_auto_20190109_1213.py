# Generated by Django 2.0.10 on 2019-01-09 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Details_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subgenre',
            old_name='Genre',
            new_name='genre',
        ),
    ]