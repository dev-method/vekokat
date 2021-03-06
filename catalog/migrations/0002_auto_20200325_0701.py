# Generated by Django 2.1.4 on 2020-03-25 07:01

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalCatFoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='media/', verbose_name='Фото')),
                ('img_webp', models.CharField(blank=True, max_length=600, null=True, verbose_name='WEBP | Фото')),
            ],
            options={
                'verbose_name': 'Фото для типа катализатора',
                'verbose_name_plural': 'Фото для типа катализатора',
            },
        ),
        migrations.CreateModel(
            name='CatalyzatorCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seotitle', models.CharField(blank=True, max_length=300, null=True, verbose_name='Seo-title')),
                ('alt_seotitle', models.CharField(blank=True, max_length=300, null=True, verbose_name='Альтернативный Seo-title')),
                ('seodescript', models.CharField(blank=True, max_length=3000, null=True, verbose_name='Seo-description')),
                ('alt_seodescript', models.CharField(blank=True, max_length=3000, null=True, verbose_name='Альтернативный Seo-description')),
                ('seokeywords', models.CharField(blank=True, max_length=3000, null=True, verbose_name='Seo-keywords')),
                ('alt_seokeywords', models.CharField(blank=True, max_length=3000, null=True, verbose_name='Альтернативный Seo-keywords')),
                ('title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Название')),
                ('alt_title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Альтернативное Название')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Основной текст')),
                ('alt_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Альтернативный текст')),
            ],
            options={
                'verbose_name': 'Тип катализатора',
                'verbose_name_plural': 'Типы катализаторов',
            },
        ),
        migrations.AlterModelOptions(
            name='catalizatortype',
            options={'verbose_name': 'Тип', 'verbose_name_plural': 'Тип'},
        ),
        migrations.AddField(
            model_name='autocatalog',
            name='image_webp',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='WEBP | Изображение'),
        ),
        migrations.AddField(
            model_name='autocatalog',
            name='seodescript',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='Seo-description'),
        ),
        migrations.AddField(
            model_name='autocatalog',
            name='seokeywords',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='Seo-keywords'),
        ),
        migrations.AddField(
            model_name='autocatalog',
            name='seotitle',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Seo-title'),
        ),
        migrations.AddField(
            model_name='autocatalog',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='autocatalog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.CatalizatorType', verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='catalcatfoto',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.CatalyzatorCategory', verbose_name='Тип катализатора'),
        ),
        migrations.AddField(
            model_name='autocatalog',
            name='cat_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.CatalyzatorCategory', verbose_name='Тип катализатора'),
            preserve_default=False,
        ),
    ]
