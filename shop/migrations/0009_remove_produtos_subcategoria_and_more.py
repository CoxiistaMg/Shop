# Generated by Django 4.0.6 on 2022-07-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_categoriasecundaria_remove_categoria_tier_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='subcategoria',
        ),
        migrations.AddField(
            model_name='categoriasecundaria',
            name='produtos',
            field=models.ManyToManyField(related_name='produtos', to='shop.produtos'),
        ),
        migrations.AlterField(
            model_name='categoriasecundaria',
            name='relacionamento',
            field=models.ManyToManyField(related_name='tags', to='shop.produtos'),
        ),
    ]