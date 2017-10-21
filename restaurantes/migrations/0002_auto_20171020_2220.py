# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='adress',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='fund_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
