# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
