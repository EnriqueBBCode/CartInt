# Generated by Django 5.0 on 2024-01-02 16:49

import Main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(upload_to=Main.models.about_us, verbose_name='Image / Imagen'),
        ),
        migrations.AlterField(
            model_name='services_item',
            name='detail',
            field=models.TextField(verbose_name='Details / Detalles'),
        ),
        migrations.AlterField(
            model_name='services_item',
            name='image',
            field=models.ImageField(upload_to=Main.models.si_img, verbose_name='Image / Imagen'),
        ),
        migrations.AlterField(
            model_name='services_item',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Name / Nombre'),
        ),
        migrations.AlterField(
            model_name='track',
            name='btn',
            field=models.CharField(max_length=250, verbose_name='Track Button / Boton de Encontrar'),
        ),
        migrations.AlterField(
            model_name='track',
            name='image',
            field=models.ImageField(upload_to=Main.models.track_img, verbose_name='Image / Imagen'),
        ),
        migrations.AlterField(
            model_name='track',
            name='number_text',
            field=models.CharField(max_length=250, verbose_name='Traking Number Text / Texto de Encontrar Carga'),
        ),
    ]