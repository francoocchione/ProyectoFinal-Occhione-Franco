# Generated by Django 4.2.3 on 2023-08-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='aves',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]