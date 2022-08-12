# Generated by Django 4.0.6 on 2022-07-21 19:56

from django.db import migrations
import shop.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_categoriasecundaria_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriasecundaria',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=shop.models.filename, variations={'thumbmail': (400, 400, False)}),
        ),
    ]
