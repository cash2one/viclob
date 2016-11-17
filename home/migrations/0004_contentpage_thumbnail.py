# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0015_fill_filter_spec_field'),
        ('home', '0003_auto_20161116_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]