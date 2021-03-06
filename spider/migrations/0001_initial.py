# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-28 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('time', models.CharField(blank=True, max_length=255, null=True)),
                ('depth', models.IntegerField(blank=True, null=True)),
                ('process', models.IntegerField(blank=True, null=True)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('mysql', models.CharField(blank=True, max_length=255, null=True)),
                ('redis', models.CharField(blank=True, max_length=255, null=True)),
                ('starttime', models.CharField(blank=True, max_length=255, null=True)),
                ('runtime', models.CharField(blank=True, max_length=255, null=True)),
                ('runtype', models.CharField(blank=True, max_length=255, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'task',
                'managed': False,
            },
        ),
    ]
