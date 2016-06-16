# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('industry', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
                ('edu', models.CharField(choices=[('DP', 'Diploma'), ('Bsc', "Bachelor's Degree"), ('Msc', "Master's Degree"), ('Phd', 'Post Graduate')], max_length=50, verbose_name='Minimum Education Level')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.RecruiterProfile')),
                ('skills', models.ManyToManyField(to='accounts.JobSkill')),
            ],
        ),
        migrations.AddField(
            model_name='jobmatch',
            name='job_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kazi.JobProfile'),
        ),
        migrations.AddField(
            model_name='jobmatch',
            name='job_seekers',
            field=models.ManyToManyField(to='accounts.JobSeekerProfile'),
        ),
        migrations.AddField(
            model_name='jobmatch',
            name='recruiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.RecruiterProfile'),
        ),
    ]
