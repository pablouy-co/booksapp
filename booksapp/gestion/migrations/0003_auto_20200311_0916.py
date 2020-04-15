# Generated by Django 2.2.5 on 2020-03-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20200309_1403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('o', 'En prestamo'), ('a', 'Disponible'), ('r', 'Reservado')], default='a', help_text='Disponibilidad del libro', max_length=1),
        ),
    ]
