# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 13:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=20)),
                ('idade_minima', models.IntegerField()),
                ('idade_maxima', models.IntegerField()),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('data_inicio', models.DateTimeField(blank=True)),
                ('data_fim', models.DateTimeField(blank=True)),
                ('local', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=20)),
                ('cep', models.IntegerField()),
                ('endereço', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=50)),
                ('administradores', models.ManyToManyField(related_name='administradores', to=settings.AUTH_USER_MODEL)),
                ('participantes', models.ManyToManyField(related_name='participantes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
