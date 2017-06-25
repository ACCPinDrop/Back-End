# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 14:57
from __future__ import unicode_literals

import django.core.validators
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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event_name', models.CharField(max_length=50)),
                ('event_date', models.DateField()),
                ('event_start_time', models.TimeField()),
                ('event_end_time', models.TimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_name', models.CharField(max_length=50, unique=True)),
                ('group_description', models.TextField()),
                ('group_picture', models.ImageField(null=True, upload_to='images/%Y-%m-%d/')),
                ('group_categories', models.ManyToManyField(to='rapipd.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('venue_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organizer_email', models.EmailField(max_length=254, unique=True)),
                ('organizer_first_name', models.CharField(blank=True, max_length=20)),
                ('organizer_last_name', models.CharField(blank=True, max_length=50)),
                ('organizer_cellphone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='group',
            name='group_organizers',
            field=models.ManyToManyField(to='rapipd.Organizer'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rapipd.Group'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rapipd.Location'),
        ),
    ]