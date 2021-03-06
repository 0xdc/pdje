# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 10:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='DkimDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selector', models.CharField(max_length=63)),
                ('private_key', models.TextField()),
                ('public_key', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, unique=True)),
                ('relay', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=192)),
                ('action', models.CharField(choices=[('REJECT', 'REJECT'), ('DEFER', 'DEFER'), ('421', '421'), ('521', '521')], max_length=8)),
                ('message', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='SenderCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=106)),
                ('relayhost', models.CharField(max_length=192)),
                ('domain_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdje.Domain', to_field='name')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=106)),
            ],
        ),
        migrations.AddField(
            model_name='dkimdomain',
            name='domain_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdje.Domain', to_field='name'),
        ),
        migrations.AddField(
            model_name='alias',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdje.Domain'),
        ),
        migrations.AddField(
            model_name='alias',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdje.User'),
        ),
    ]
