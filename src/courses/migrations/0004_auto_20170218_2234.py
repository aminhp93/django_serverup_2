# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 22:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170218_2231'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lecture',
            unique_together=set([('slug', 'course')]),
        ),
    ]
