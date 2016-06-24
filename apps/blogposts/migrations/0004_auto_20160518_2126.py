# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-18 21:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0003_auto_20160517_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='blog_headline',
            field=models.TextField(default=datetime.datetime(2016, 5, 18, 21, 26, 37, 522131, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='blog_image',
            field=models.TextField(default=datetime.datetime(2016, 5, 18, 21, 26, 50, 21559, tzinfo=utc)),
            preserve_default=False,
        ),
    ]