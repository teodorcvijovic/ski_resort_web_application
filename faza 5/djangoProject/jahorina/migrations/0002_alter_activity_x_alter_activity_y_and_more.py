# Generated by Django 4.0.4 on 2022-05-21 22:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jahorina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='x',
            field=models.DecimalField(decimal_places=20, default=0.0, max_digits=21),
        ),
        migrations.AlterField(
            model_name='activity',
            name='y',
            field=models.DecimalField(decimal_places=20, default=0.0, max_digits=21),
        ),
        migrations.AlterField(
            model_name='skitrack',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 22, 0, 58, 40, 909602)),
        ),
    ]