# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-10 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=512)),
                ('trade_location', models.CharField(max_length=32)),
                ('price', models.FloatField(default=0)),
                ('picture', models.ImageField(upload_to='goods')),
                ('seller', models.CharField(max_length=50)),
                ('seller_phone', models.IntegerField()),
                ('seller_qq', models.IntegerField()),
                ('publish_time', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SecondHand.Category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('time', models.DateField()),
            ],
        ),
    ]
