# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171110_0238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
        migrations.AddField(
            model_name='post',
            name='postimage',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430'),
        ),
    ]
