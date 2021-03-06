# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 03:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields
import userena.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.CharField(blank=True, max_length=255)),
                ('level', models.CharField(choices=[('Nv', 'Novice'), ('In', 'Intermediate'), ('Ex', 'Expert')], max_length=50, verbose_name='Level of Mastery')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mugshot', easy_thumbnails.fields.ThumbnailerImageField(blank=True, help_text='A personal image displayed in your profile.', upload_to=userena.models.upload_to_mugshot, verbose_name='mugshot')),
                ('privacy', models.CharField(choices=[('open', 'Open'), ('registered', 'Registered'), ('closed', 'Closed')], default='registered', help_text='Designates who can view your profile.', max_length=15, verbose_name='privacy')),
                ('about', models.CharField(max_length=100)),
            ],
            options={
                'permissions': (('view_profile', 'Can view profile'),),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobSeekerProfile',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.UserProfile')),
                ('dob', models.DateField(verbose_name='date of birth')),
                ('mobile', models.CharField(max_length=20)),
                ('experience', models.IntegerField()),
                ('industry', models.CharField(max_length=100)),
                ('edu', models.CharField(choices=[('DP', 'Diploma'), ('Bsc', "Bachelor's Degree"), ('Msc', "Master's Degree"), ('Phd', 'Post Graduate')], max_length=50, verbose_name='Education Level')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=50)),
                ('location', models.CharField(max_length=100, verbose_name='Area of Residence')),
                ('skills', models.ManyToManyField(to='accounts.JobSkill')),
            ],
            options={
                'permissions': (('view_profile', 'Can view profile'),),
                'abstract': False,
            },
            bases=('accounts.userprofile',),
        ),
        migrations.CreateModel(
            name='RecruiterProfile',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.UserProfile')),
                ('company', models.CharField(max_length=100)),
            ],
            options={
                'permissions': (('view_profile', 'Can view profile'),),
                'abstract': False,
            },
            bases=('accounts.userprofile',),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
