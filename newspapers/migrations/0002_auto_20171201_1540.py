# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspapers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaper',
            name='nume',
            field=models.CharField(max_length=40),
        ),
    ]
