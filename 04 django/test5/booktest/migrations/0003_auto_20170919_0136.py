# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20170918_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='booktest/')),
            ],
        ),
        migrations.AlterField(
            model_name='areainfo',
            name='aParent',
            field=models.ForeignKey(null=True, to='booktest.AreaInfo', blank=True),
        ),
    ]
