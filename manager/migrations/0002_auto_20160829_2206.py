# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 20:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speciality',
            old_name='field_id',
            new_name='field',
        ),
    ]
