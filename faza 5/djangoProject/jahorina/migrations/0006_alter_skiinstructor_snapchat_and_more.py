# Generated by Django 4.0.4 on 2022-05-24 01:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jahorina', '0005_alter_skiinstructor_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skiinstructor',
            name='snapchat',
            field=models.CharField(blank=True, max_length=290, null=True),
        ),
        migrations.AlterField(
            model_name='skitrack',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 24, 3, 52, 2, 298398)),
        ),
    ]
