# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20151107_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('fecha_in', models.DateTimeField(auto_now_add=True)),
                ('fecha_out', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
