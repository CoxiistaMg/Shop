# Generated by Django 4.0.6 on 2022-07-29 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_review_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='comentario',
            field=models.TextField(default=1, verbose_name='Comentários'),
            preserve_default=False,
        ),
    ]