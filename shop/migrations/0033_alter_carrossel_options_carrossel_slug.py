# Generated by Django 4.0.6 on 2022-08-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0032_remove_produto_categoria_produto_categoria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrossel',
            options={'verbose_name': 'Carrossel', 'verbose_name_plural': 'Carrossel'},
        ),
        migrations.AddField(
            model_name='carrossel',
            name='slug',
            field=models.SlugField(default=1, editable=False, max_length=100),
            preserve_default=False,
        ),
    ]