# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 17:01
from __future__ import unicode_literals

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20170219_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='order',
            field=courses.fields.PositionField(default=-1),
        ),
    ]
