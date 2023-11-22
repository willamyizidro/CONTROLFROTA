# Generated by Django 4.2.6 on 2023-10-29 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0006_tipomanutencao_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipomanutencao',
            name='produto',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='tipomanutencao',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]