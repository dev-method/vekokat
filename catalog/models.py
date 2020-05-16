# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.admin import AdminThumbnail
from PIL import Image
import os, time
from celery import shared_task
from django.db.models.signals import post_save
from django.dispatch import receiver

media_path = '/usr/src/vekokat.ru/vekokat_ver2/media/media/'
app_url = '/usr/src/vekokat.ru/vekokat_ver2'
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
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    image=ProcessedImageField(verbose_name='Изображение',upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90},
                                           null = True, blank = True)
    image_low = ImageSpecField(source='image',
                               format='JPEG',
                               options={'quality': 1})
    image_webp = models.CharField(verbose_name='WEBP | Изображение', max_length=600, null=True, blank=True)
    image_jp2 = models.CharField(verbose_name='JPEG2000 | Изображение', max_length=600, null=True, blank=True)
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
        if self.cat_type_id==2:
            return "/catalog/importnye/%s/" % self.slug
        elif self.cat_type_id==1:
            return "/catalog/otechestvennyj/%s/" % self.slug

class CatalogInline(admin.TabularInline):
    model = AutoCatalog

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('__str__','admin_thumbnail', 'category')
    list_per_page = 20
    admin_thumbnail = AdminThumbnail(image_field='avatarimage')
    tabular=[CatalogInline]
    fieldsets = [
        (None, {'fields': ['auto_model', 'year', 'weight', 'price_kg', 'sum', 'cat_type']}),
        ('SEO', {'fields': ['seotitle', 'seodescript', 'seokeywords'],
                 'classes': ['collapse']}),
        ('Изображения', {'fields': ['image', 'image_webp', 'image_jp2'], 'classes': ['collapse']}),
    ]

@shared_task(acks_late=True)
def catalog_alter_formats(pk):
    time.sleep(1.5)
    catalog_item = AutoCatalog.objects.get(pk=pk)
    origin_name = os.path.basename(catalog_item.image.url)
    clear_name = origin_name.split('.')[0]
    Image.open(media_path+origin_name).save(media_path+clear_name+'.webp', 'webp', quality='70')
    Image.open(media_path + origin_name).save(media_path + clear_name + '.jpx', quality_mode='dB', quality_layers=[34])
    catalog_item.image_webp = '/media/media/' + clear_name+'.webp'
    catalog_item.image_jp2 = '/media/media/' + clear_name + '.jpx'
    catalog_item.save()

@receiver(post_save, sender= AutoCatalog)
def methods_image(sender, instance, created, raw, using, **kwargs):
    if instance.image_webp and instance.image_jp2:
        if not os.path.isfile(app_url+instance.image_webp):
            catalog_alter_formats(instance.pk)
        elif not os.path.isfile(app_url+instance.image_jp2):
            catalog_alter_formats(instance.pk)
        else:
            pass
    elif instance.image:
        catalog_alter_formats(instance.pk)
    else:
        pass

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
    amp_text = RichTextUploadingField('AMP-вариант | Основной текст', null=True, blank=True)
    alt_text = RichTextUploadingField('Альтернативный текст', null=True, blank=True)
    amp_alt_text = RichTextUploadingField('AMP-вариант | Альтернативный текст', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = ('ТИП КАТАЛИЗАТОРА')
        verbose_name_plural = ('ТИПЫ КАТАЛИЗАТОРОВ')

    def __str__(self):
        return u'%s' % self.title
    def get_absolute_url(self):
        return "/catalizators/%s/" % self.slug

class CatalyzatorCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'alt_title', 'slug', 'text', 'alt_text',]}),
        ('SEO', {'fields': ['seotitle', 'alt_seotitle', 'seodescript', 'alt_seodescript', 'seokeywords', 'alt_seokeywords'],
                 'classes': ['collapse']}),
        ('AMP-текста', {'fields': ['amp_text', 'amp_alt_text'],'classes': ['collapse']}),
    ]

class CatalCatFoto(models.Model):
    img=ProcessedImageField(verbose_name='Фото', upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90}, blank=True, null=True)
    img_low=ImageSpecField(source='img',
                                 format='JPEG',
                                 options={'quality': 1})
    img_webp = models.CharField(verbose_name='WEBP | Фото', max_length=600, null=True, blank=True)
    img_jp2 = models.CharField(verbose_name='JPEG2000 | Фото', max_length=600, null=True, blank=True)
    avatarimage = ImageSpecField(source='img',
                                 processors=[ResizeToFill(100, 100)],
                                 format='JPEG',
                                 options={'quality': 50})
    position=models.ForeignKey('CatalyzatorCategory', verbose_name="Тип катализатора", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('ФОТО К ТИПУ КАТАЛИЗАТОРА')
        verbose_name_plural = ('ФОТО К ТИПУ КАТАЛИЗАТОРА')

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

@shared_task(acks_late=True)
def catfoto_alter_formats(pk):
    time.sleep(1.5)
    catalog_item = CatalCatFoto.objects.get(pk=pk)
    origin_name = os.path.basename(catalog_item.img.url)
    clear_name = origin_name.split('.')[0]
    Image.open(media_path+origin_name).save(media_path+clear_name+'.webp', 'webp', quality='70')
    Image.open(media_path + origin_name).save(media_path + clear_name + '.jpx', quality_mode='dB', quality_layers=[34])
    catalog_item.img_webp = '/media/media/' + clear_name+'.webp'
    catalog_item.img_jp2 = '/media/media/' + clear_name + '.jpx'
    catalog_item.save()

@receiver(post_save, sender= CatalCatFoto)
def catfoto_method(sender, instance, created, raw, using, **kwargs):
    if instance.img_webp and instance.img_jp2:
        if not os.path.isfile(app_url+instance.img_webp):
            catfoto_alter_formats(instance.pk)
        elif not os.path.isfile(app_url+instance.img_jp2):
            catfoto_alter_formats(instance.pk)
        else:
            pass
    elif instance.img:
        catfoto_alter_formats(instance.pk)
    else:
        pass