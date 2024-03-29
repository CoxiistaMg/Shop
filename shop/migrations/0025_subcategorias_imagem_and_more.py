# Generated by Django 4.0.6 on 2022-07-21 20:32

from django.db import migrations, models
import shop.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_alter_relacionamentosubcategoria_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategorias',
            name='imagem',
            field=stdimage.models.StdImageField(default=1, force_min_size=False, upload_to=shop.models.filename, variations={'thumb': (400, 400, True)}),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='relacionamentosubcategoria',
            name='nome',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nome'),
        ),
    ]
