# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-29 10:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0009_auto_20171228_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='company_name',
        ),
    ]
