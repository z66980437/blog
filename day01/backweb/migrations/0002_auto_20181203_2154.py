# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-03 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]