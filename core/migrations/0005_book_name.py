# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-16 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_person_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
