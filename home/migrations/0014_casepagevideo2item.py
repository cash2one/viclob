# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-07 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_contactpage_telephone2'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasePageVideo2Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u89c6\u9891\u540d\u79f0')),
                ('code', wagtail.wagtailcore.fields.StreamField([(b'code', wagtail.wagtailcore.blocks.RawHTMLBlock())])),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='case2_videos', to='home.CasePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]