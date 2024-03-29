# Generated by Django 4.0.6 on 2022-07-18 16:13

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_categoria_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrossel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('descricao', models.TextField(max_length=1000)),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='', variations={})),
            ],
        ),
        migrations.AlterModelOptions(
            name='produtos',
            options={'verbose_name': 'Produto '},
        ),
        migrations.AddField(
            model_name='produtos',
            name='informacao',
            field=models.TextField(default=1, verbose_name='Informações'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produtos',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço'),
        ),
    ]
