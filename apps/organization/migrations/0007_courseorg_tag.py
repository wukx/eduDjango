# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-10 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_teacher_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='\u5168\u56fd\u51fa\u540d', max_length=4, verbose_name='\u673a\u6784\u6807\u7b7e'),
        ),
    ]
