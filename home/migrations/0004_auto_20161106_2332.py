# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 15:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20161106_2327'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DistributeSelfMediaItem',
            new_name='DistributePageSelfMediaItem',
        ),
    ]