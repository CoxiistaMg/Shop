# Generated by Django 4.0.6 on 2022-07-12 21:25

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_produtos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='icon',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='icons/', variations={'thumb': (30, 30, True)}),
        ),
    ]
