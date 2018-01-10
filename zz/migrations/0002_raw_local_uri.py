# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('zz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='raw',
            name='local_uri',
            field=models.CharField(default=datetime.datetime(2018, 1, 5, 9, 4, 50, 153607, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
