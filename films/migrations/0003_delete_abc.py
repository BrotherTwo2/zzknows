# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_abc'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ABC',
        ),
    ]
