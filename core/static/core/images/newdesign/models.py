# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.admin import AdminThumbnail

# Create your models here.

class AutoCatalog(models.Model):
    seotitle = models.CharField('Seo-title', null=True, blank=True, max_length=300)
    seodescript = models.CharField('Seo-description', null=True, blank=True, max_length=3000)
    seokeywords = models.CharField('Seo-keywords', null=True, blank=True, max_length=3000)
    slug = models.SlugField(blank=True, null=True)
    auto_model = models.CharField('Модель автомобиля', max_length=1000, null=True, blank=True)
    year = models.CharField('Год выпуска', max_length=10, null=True, blank=True)
    weight = models.CharField('Вес катализатора', max_length=100, null=True, blank=True)
    price_kg = models.CharField('Цена за кг', max_length=500, null=True, blank=True)
    sum = models.CharField('Сумма', max_length=500, null=True, blank=True)
    image=ProcessedImageField(verbose_name='Изображение',upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90},
                                           null = True, blank = True)
    image_low = ImageSpecField(source='image',
                               format='JPEG',
                               options={'quality': 1})
    image_webp = models.CharField(verbose_name='WEBP | Изображение', max_length=600, null=True, blank=True)
    avatarimage = ImageSpecField(source='image',
                                 processors=[ResizeToFill(100, 100)],
                                 format='JPEG',
                                 options={'quality': 50})
    category = models.ForeignKey('CatalizatorType', verbose_name="Тип",
                                 on_delete=models.CASCADE)
    cat_type = models.ForeignKey('CatalyzatorCategory', verbose_name="Тип катализатора",
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('КАТАЛОГ | Автокатализатор')
        verbose_name_plural = ('КАТАЛОГ | Автокатализаторы')

    def __str__(self):
        return u'%s' % self.auto_model

    def save(self, *args, **kwargs):
        return super(AutoCatalog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/catalog/%s/" % self.slug

class CatalogInline(admin.TabularInline):
    model = AutoCatalog

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('__str__','admin_thumbnail', 'category')
    list_per_page = 20
    admin_thumbnail = AdminThumbnail(image_field='avatarimage')
    tabular=[CatalogInline]

class CatalizatorType(models.Model):
    type = models.CharField('Тип катализатора', max_length=500, null=True, blank=True)
    class Meta:
        verbose_name = ('Тип')
        verbose_name_plural = ('Тип')

    def __str__(self):
        return u'%s' % self.type

class CatalyzatorCategory(models.Model):
    seotitle = models.CharField('Seo-title', null=True, blank=True, max_length=300)
    alt_seotitle = models.CharField('Альтернативный Seo-title', null=True, blank=True, max_length=300)
    seodescript = models.CharField('Seo-description', null=True, blank=True, max_length=3000)
    alt_seodescript = models.CharField('Альтернативный Seo-description', null=True, blank=True, max_length=3000)
    seokeywords = models.CharField('Seo-keywords', null=True, blank=True, max_length=3000)
    alt_seokeywords = models.CharField('Альтернативный Seo-keywords', null=True, blank=True, max_length=3000)
    title = models.CharField('Название', null=True, blank=True, max_length=300)
    alt_title = models.CharField('Альтернативное Название', null=True, blank=True, max_length=300)
    slug = models.SlugField(blank=True, null=True)
    text=RichTextUploadingField('Основной текст', null=True, blank=True)
    alt_text = RichTextUploadingField('Альтернативный текст', null=True, blank=True)

    class Meta:
        verbose_name = ('Тип катализатора')
        verbose_name_plural = ('Типы катализаторов')

    def __str__(self):
        return u'%s' % self.title
    def get_absolute_url(self):
        return "/catalizators/%s/" % self.slug

class CatalCatFoto(models.Model):
    img=ProcessedImageField(verbose_name='Фото', upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90}, blank=True, null=True)
    img_low=ImageSpecField(source='img',
                                 format='JPEG',
                                 options={'quality': 1})
    img_webp = models.CharField(verbose_name='WEBP | Фото', max_length=600, null=True, blank=True)
    avatarimage = ImageSpecField(source='img',
                                 processors=[ResizeToFill(100, 100)],
                                 format='JPEG',
                                 options={'quality': 50})
    position=models.ForeignKey('CatalyzatorCategory', verbose_name="Тип катализатора", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Фото для типа катализатора')
        verbose_name_plural = ('Фото для типа катализатора')

    def __str__(self):
        self.title = "Фото"
        return u'%s' % self.title

class CatalCatFotoInline(admin.TabularInline):
    model = CatalCatFoto

class CatalCatFotoAdmin(admin.ModelAdmin):
    list_display = ('__str__','admin_thumbnail',  'position')
    list_per_page = 20
    admin_thumbnail = AdminThumbnail(image_field='avatarimage')
    tabular=[CatalCatFotoInline]