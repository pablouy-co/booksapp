# Generated by Django 2.2.5 on 2020-03-12 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0009_auto_20200312_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='imagen',
            new_name='image',
        ),
    ]
