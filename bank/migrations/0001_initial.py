# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Bank ID')),
                ('name', models.CharField(max_length=50, verbose_name='Bank Name')),
            ],
            options={
                'verbose_name': 'Bank',
                'verbose_name_plural': 'Banks',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=11)),
                ('branch', models.CharField(max_length=75, verbose_name='Branch')),
                ('address', models.CharField(max_length=195, verbose_name='Address')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('district', models.CharField(max_length=50, verbose_name='District')),
                ('state', models.CharField(max_length=26, verbose_name='State')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_branches', to='bank.Bank')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
            },
        ),
    ]
