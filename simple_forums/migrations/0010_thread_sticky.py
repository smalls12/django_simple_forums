# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_forums', '0009_topic_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='sticky',
            field=models.BooleanField(default=False),
        ),
    ]