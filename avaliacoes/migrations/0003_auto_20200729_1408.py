# Generated by Django 3.0.8 on 2020-07-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0002_auto_20200729_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]