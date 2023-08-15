# Generated by Django 4.2.3 on 2023-08-11 16:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('subtitulo', models.CharField(max_length=150)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('autor', models.CharField(max_length=150)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Aves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.CharField(max_length=200)),
                ('familia', models.CharField(max_length=200)),
                ('especie', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('caracteristicas', models.TextField()),
                ('ultima_observacion', models.DateField()),
            ],
        ),
    ]