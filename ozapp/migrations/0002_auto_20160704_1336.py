# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ozapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='endereço',
            new_name='endereco',
        ),
    ]