# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-07 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20170107_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='telephone2',
            field=models.CharField(blank=True, max_length=20, verbose_name='\u7535\u8bdd2'),
        ),
    ]
