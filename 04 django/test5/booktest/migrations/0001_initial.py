# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('atitle', models.CharField(max_length=30)),
                ('aParent', models.ForeignKey(to='booktest.AreaInfo', null=True)),
            ],
        ),
    ]
