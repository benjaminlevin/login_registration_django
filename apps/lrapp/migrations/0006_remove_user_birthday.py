# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-26 20:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lrapp', '0005_auto_20170726_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
    ]