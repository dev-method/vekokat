# Generated by Django 2.1.4 on 2020-04-21 17:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conditions',
            name='text_part1_amp',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст - AMP- вариант| Часть1'),
        ),
        migrations.AddField(
            model_name='conditions',
            name='text_part2_amp',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст - AMP- вариант| Часть2'),
        ),
    ]
