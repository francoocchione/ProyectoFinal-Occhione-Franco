# Generated by Django 4.2.3 on 2023-08-15 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0005_remove_aves_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='aves',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='audio/'),
        ),
    ]
