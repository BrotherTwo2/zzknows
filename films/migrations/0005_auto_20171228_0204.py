# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_films_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='fresh',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('oss', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='mature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('orignal', models.CharField(max_length=100)),
                ('processed', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Films',
        ),
    ]
