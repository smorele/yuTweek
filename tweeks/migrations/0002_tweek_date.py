# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tweeks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweek',
            name='date',
            field=models.DateTimeField(default=datetime.date(2015, 5, 25), auto_now_add=True),
            preserve_default=False,
        ),
    ]
