# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdje', '0002_auto_20170425_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='relay',
            field=models.BooleanField(default=False),
        ),
    ]
