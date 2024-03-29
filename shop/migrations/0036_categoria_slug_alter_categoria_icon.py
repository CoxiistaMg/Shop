# Generated by Django 4.0.6 on 2022-08-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0035_alter_categoria_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoria',
            name='icon',
            field=models.CharField(choices=[('fas fa-gamepad', 'console'), ('fas fa-chess', 'jogos'), ('fab fa-playstation', 'playstation'), ('fab fa-xbox', 'xbox')], max_length=20),
        ),
    ]
