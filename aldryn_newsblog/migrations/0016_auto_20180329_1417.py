# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-29 12:17
from __future__ import unicode_literals

import aldryn_apphooks_config.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


TEMPLATE_PREFIX_CHOICES = getattr(
    settings,
    'ALDRYN_NEWSBLOG_TEMPLATE_PREFIXES',
    [],
)


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0015_auto_20161208_0403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsblogconfig',
            options={'verbose_name': 'Section', 'verbose_name_plural': 'Sections'},
        ),
        migrations.AlterModelOptions(
            name='newsblogconfigtranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'Section Translation'},
        ),
        migrations.AlterField(
            model_name='article',
            name='app_config',
            field=aldryn_apphooks_config.fields.AppHookConfigField(help_text='When selecting a value, the form is reloaded to get the updated default', on_delete=django.db.models.deletion.CASCADE, to='aldryn_newsblog.NewsBlogConfig', verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='article',
            name='featured_image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='featured image'),
        ),
        migrations.AlterField(
            model_name='newsblogconfig',
            name='namespace',
            field=models.CharField(default=None, max_length=100, unique=True, verbose_name='Instance namespace'),
        ),
        migrations.AlterField(
            model_name='newsblogconfig',
            name='template_prefix',
            field=models.CharField(blank=True, choices=TEMPLATE_PREFIX_CHOICES, max_length=20, null=True, verbose_name='Prefix for template dirs'),
        ),
        migrations.AlterField(
            model_name='newsblogconfig',
            name='type',
            field=models.CharField(max_length=100, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='newsblogconfigtranslation',
            name='app_title',
            field=models.CharField(max_length=234, verbose_name='name'),
        ),
    ]
