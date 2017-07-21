# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_ip', models.CharField(blank=True, default='0.0.0.0', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('label', models.CharField(blank=True, default='Elektron', max_length=100)),
                ('state', models.CharField(blank=True, default='Off', max_length=100)),
                ('measure', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
