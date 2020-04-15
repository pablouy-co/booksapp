# Generated by Django 2.2.5 on 2020-03-27 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0024_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestion.Book', verbose_name='Libro'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(verbose_name='Comentario (máx. 350 caracteres'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Clasificación'),
        ),
    ]
