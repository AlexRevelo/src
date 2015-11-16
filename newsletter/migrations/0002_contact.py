# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=120, null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
    ]
