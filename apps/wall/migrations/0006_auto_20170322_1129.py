# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0005_auto_20170322_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secret',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='login.User'),
        ),
    ]