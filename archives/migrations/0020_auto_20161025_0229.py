# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 18:29
from __future__ import unicode_literals

import archives.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0019_auto_20161023_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=archives.models.generate_image_filename, validators=[archives.models.check_image_extension], verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='file',
            field=models.ImageField(blank=True, upload_to=archives.models.generate_image_filename, validators=[archives.models.check_image_extension], verbose_name='图片'),
        ),
    ]
