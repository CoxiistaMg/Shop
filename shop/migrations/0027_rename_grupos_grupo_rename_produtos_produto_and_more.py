# Generated by Django 4.0.6 on 2022-07-21 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_grupos_delete_relacionamentosubcategoria'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Grupos',
            new_name='Grupo',
        ),
        migrations.RenameModel(
            old_name='Produtos',
            new_name='Produto',
        ),
        migrations.RenameModel(
            old_name='SubCategorias',
            new_name='SubCategoria',
        ),
    ]
