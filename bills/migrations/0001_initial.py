# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='counter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.DecimalField(max_digits=10, decimal_places=0)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='counter_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DecimalField(max_digits=12, decimal_places=0)),
                ('reg_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('counter', models.ForeignKey(to='bills.counter')),
            ],
        ),
        migrations.CreateModel(
            name='counter_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='counter',
            name='counter_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='bills.counter_type', null=True),
        ),
    ]
