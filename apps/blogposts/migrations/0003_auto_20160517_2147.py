# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-17 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0002_blogs_blog_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_author', models.TextField()),
                ('blog_article', models.TextField()),
                ('blog_date', models.DateField()),
            ],
            options={
                'db_table': 'Articles',
            },
        ),
        migrations.DeleteModel(
            name='Blogs',
        ),
    ]
