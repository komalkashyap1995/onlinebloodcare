# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-28 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0003_auto_20180425_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspiringstories',
            name='Story',
            field=models.CharField(max_length=600),
        ),
    ]
