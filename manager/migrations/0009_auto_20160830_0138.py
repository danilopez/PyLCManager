# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_auto_20160830_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='home_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]