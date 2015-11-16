# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contact',
        ),
        migrations.AddField(
            model_name='signup',
            name='mensaje',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
