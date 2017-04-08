# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-02 10:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MMW', '0002_auto_20170327_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhoIAm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.TextField(max_length=128, null=True, verbose_name='what is important to me?')),
                ('text2', models.TextField(max_length=128, null=True, verbose_name='What do i like about myself?')),
                ('text3', models.TextField(max_length=64, null=True, verbose_name='What do other people like about me?')),
                ('text4', models.TextField(max_length=128, null=True, verbose_name='How to best support me:')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='text1',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='text2',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='text3',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='text4',
        ),
    ]
