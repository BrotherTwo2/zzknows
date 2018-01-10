# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_delete_abc'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='url',
            field=models.CharField(default=datetime.datetime(2017, 12, 26, 11, 22, 25, 889662, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
