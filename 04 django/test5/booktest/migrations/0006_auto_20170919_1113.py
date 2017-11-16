# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0005_auto_20170919_1112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='pbub_date',
            new_name='bpub_date',
        ),
    ]
