# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20170224_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mycourse',
            options={'verbose_name': 'My course', 'verbose_name_plural': 'My courses'},
        ),
        migrations.AddField(
            model_name='lecture',
            name='free',
            field=models.BooleanField(default=False),
        ),
    ]
