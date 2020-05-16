# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.admin import AdminThumbnail
from PIL import Image
import os, time
from celery import shared_task
from django.db.models.signals import post_save
from django.dispatch import receiver

media_path = '/usr/src/vekokat.ru/vekokat_ver2/media/media/'
# Create your models here.

class MainSeo(models.Model):
    title=models.TextField('title', max_length=300, null=True,blank=True)
    description=models.TextField('description', max_length=1000, null=True,blank=True)
    keywords=models.TextField('keywords', max_length=1000, null=True,blank=True)
    image = ProcessedImageField(verbose_name='Изображение для OpenGraph', upload_to='media/',
                                format='JPEG',
                                options={'quality': 90},
                                null=True, blank=True)

    class Meta:
        verbose_name = ('SEO')
        verbose_name_plural = ('SEO')

    def __str__(self):
        self.title="SEO"
        return u'%s' % self.title

class NewSlider(models.Model):
    slide=ProcessedImageField(verbose_name='Фото', help_text="Фото - ширина 1920px | Формат JPEG",upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90},
                                           null = True, blank = True)
    slide_low = ImageSpecField(source='slide',
                                 format='JPEG',
                                 options={'quality': 1})
    slide_webp = models.CharField(verbose_name='WEBP | Фото',
                                  max_length=600, null=True, blank=True)
    slide_768 = ProcessedImageField(verbose_name='Фото', help_text="Фото - ширина 768px | Формат JPEG",
                                upload_to='media/',
                                format='JPEG',
                                options={'quality': 90},
                                null=True, blank=True)
    slide_768_low = ImageSpecField(source='slide_768',
                               format='JPEG',
                               options={'quality': 1})
    slide_768_webp = models.CharField(verbose_name='WEBP | Фото',
                                  max_length=600, null=True, blank=True)
    slide_576 = ProcessedImageField(verbose_name='Фото', help_text="Фото - ширина 576px | Формат JPEG",
                                    upload_to='media/',
                                    format='JPEG',
                                    options={'quality': 90},
                                    null=True, blank=True)
    slide_576_low = ImageSpecField(source='slide_576',
                                   format='JPEG',
                                   options={'quality': 1})
    slide_576_webp = models.CharField(verbose_name='WEBP | Фото',
                                      max_length=600, null=True, blank=True)
    avatarimage = ImageSpecField(source='slide',
                                 processors=[ResizeToFill(100, 100)],
                                 format='JPEG',
                                 options={'quality': 50})

    class Meta:
        verbose_name = ('Блок | Основной слайдер фото')
        verbose_name_plural = ('Блок | Основной слайдер фото')

    def __str__(self):
        self.title="Слайд"
        return u'%s' % self.title

class NewSliderInline(admin.TabularInline):
    model = NewSlider

class NewSliderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail',)
    exclude = ('slide_low', 'slide_webp', 'slide_768_low', 'slide_768_webp', 'slide_576_low', 'slide_576_webp',)
    admin_thumbnail = AdminThumbnail(image_field='avatarimage')
    tabular=[NewSliderInline]

@shared_task(acks_late=True)
def newslide_create_webp(pk):
    time.sleep(1.5)
    newslide = NewSlider.objects.get(pk=pk)
    slide_name = os.path.basename(newslide.slide.url)
    slide_webp_name = slide_name.split('.')[0] + '.webp'
    slide_path = media_path + slide_name
    im = Image.open(slide_path)
    im.save(media_path + slide_webp_name, 'webp', quality='20')
    newslide.slide_webp = '/media/media/' + slide_webp_name
    slide_768_name = os.path.basename(newslide.slide_768.url)
    slide_768_webp_name = slide_768_name.split('.')[0] + '.webp'
    slide_768_path = media_path + slide_768_name
    im_768 = Image.open(slide_768_path)
    im_768.save(media_path + slide_768_webp_name, 'webp', quality='20')
    newslide.slide_768_webp = '/media/media/' + slide_768_webp_name
    slide_576_name = os.path.basename(newslide.slide_576.url)
    slide_576_webp_name = slide_576_name.split('.')[0] + '.webp'
    slide_576_path = media_path + slide_576_name
    im_576 = Image.open(slide_576_path)
    im_576.save(media_path + slide_576_webp_name, 'webp', quality='20')
    newslide.slide_576_webp = '/media/media/' + slide_576_webp_name
    newslide.save()

@receiver(post_save, sender= NewSlider)
def methods_image(sender, instance, created, raw, using, **kwargs):
    if instance.slide_webp and os.path.isfile('/usr/src/vekokat.ru/vekokat_ver2'+instance.slide_webp):
        pass
    elif not instance.slide:
        pass
    else:
        newslide_create_webp(instance.pk)


class NewAdvantages(models.Model):
    icon=models.CharField(verbose_name='Код иконки FontAwesome', help_text="Имеет приоритет перед загруженным изображением", max_length=1000, null = True, blank = True)
    icon_image=ProcessedImageField(verbose_name='Изображение для иконки', help_text="Высота изображения 80px | Формат PNG",upload_to='media/',
                                           format='PNG',
                                           options={'quality': 90},
                                           null = True, blank = True)
    icon_image_hover = ProcessedImageField(verbose_name='Изображение иконки при наведении',
                                     help_text="Высота изображения 150px | Формат PNG", upload_to='media/',
                                     format='PNG',
                                     options={'quality': 90},
                                     null=True, blank=True)
    icon_image_hover_webp = models.FileField(verbose_name='WEBP | Изображение иконки при наведении',
                                  help_text="Высота изображения 150px | Формат WEBP",
                                  upload_to='media/', null=True, blank=True)
    avatarimage = ImageSpecField(source='icon_image',
                                 processors=[ResizeToFill(50, 50)],
                                 format='PNG',
                                 options={'quality': 50})
    svg = models.FileField("SVG - иконка", upload_to='uploads/', null=True)
    text=models.TextField(verbose_name='Текст преимущества', help_text="Отображается под иконкой", max_length=3000, null = True, blank = True)
    group=models.IntegerField(verbose_name="Порядок следования на сайте", null = True, blank = True)

    class Meta:
        verbose_name = ('Блок | Преимущества')
        verbose_name_plural = ('Блок | Преимущества')

    def __str__(self):
        title=self.text[0:10]+"..."
        return u'%s' % title

class NewWorkingMethods(models.Model):
    number=models.CharField(verbose_name='Номер элемента', help_text="Пример: 1.", max_length=10, null = True, blank = True)
    text=models.TextField(verbose_name='Текст элемента', max_length=2000, null = True, blank = True)
    image=ProcessedImageField(verbose_name='Изображение для элемента', help_text="Соотношение ширина/высота: 1 на 1.8 | Формат JPEG",upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90},
                                           null = True, blank = True)
    image_low = ImageSpecField(source='image',
                                 format='JPEG',
                                 options={'quality': 1})
    image_webp = models.CharField(verbose_name='WEBP | Изображение для элемента',
                                  max_length=600, null=True, blank=True)
    avatarimage = ImageSpecField(source='image',
                                 processors=[ResizeToFill(100, 100)],
                                 format='PNG',
                                 options={'quality': 50})
    group = models.IntegerField(verbose_name="Порядок следования на сайте", null=True, blank=True)

    class Meta:
        verbose_name = ('Блок | Порядок работы')
        verbose_name_plural = ('Блок | Порядок работы')

    def __str__(self):
        title=self.text[0:10]+"..."
        return u'%s' % title

class NewWorkingMethodsInline(admin.TabularInline):
    model = NewWorkingMethods

class NewWorkingMethodsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail',)
    exclude = ('image_low', 'image_webp', )
    admin_thumbnail = AdminThumbnail(image_field='avatarimage')
    tabular=[NewWorkingMethodsInline]

@shared_task(acks_late=True)
def methods_create_webp(pk):
    time.sleep(1.5)
    method = NewWorkingMethods.objects.get(pk=pk)
    img_name = os.path.basename(method.image.url)
    webp_name = img_name.split('.')[0] + '.webp'
    img_path = media_path + img_name
    im = Image.open(img_path)
    im.save(media_path + webp_name, 'webp', quality='20')
    method.image_webp = '/media/media/' + webp_name
    method.save()

@receiver(post_save, sender= NewWorkingMethods)
def methods_image(sender, instance, created, raw, using, **kwargs):
    if instance.image_webp and os.path.isfile('/usr/src/vekokat.ru/vekokat_ver2'+instance.image_webp):
        pass
    elif not instance.image:
        pass
    else:
        methods_create_webp(instance.pk)

class NewLaboratory(models.Model):
    title=models.CharField(verbose_name='Заголовок элемента', help_text="Показывается над иконкой", max_length=1000, null = True, blank = True)
    icon = models.CharField(verbose_name='Код иконки FontAwesome',
                            help_text="Имеет приоритет перед загруженным изображением", max_length=1000, null=True,
                            blank=True)
    icon_image = ProcessedImageField(verbose_name='Изображение для иконки',
                                     help_text="Высота изображения 80px | Формат PNG", upload_to='media/',
                                     format='PNG',
                                     options={'quality': 90},
                                     null=True, blank=True)
    avatarimage = ImageSpecField(source='icon_image',
                                 processors=[ResizeToFill(50, 50)],
                                 format='PNG',
                                 options={'quality': 50})
    svg = models.FileField("SVG - иконка", upload_to='uploads/', null=True)
    text=models.TextField(verbose_name='Текст элемента', help_text="Показывается под иконкой", max_length=3000, null = True, blank = True)
    group = models.IntegerField(verbose_name="Порядок следования на сайте", null=True, blank=True)


    class Meta:
        verbose_name = ('Блок | Мобильная лаборатория')
        verbose_name_plural = ('Блок | Мобильная лаборатория')

    def __str__(self):
        return u'%s' % self.title

class NewRegions(models.Model):
    icon = models.CharField(verbose_name='Код иконки FontAwesome',
                            help_text="Имеет приоритет перед загруженным изображением", max_length=1000, null=True,
                            blank=True)
    icon_image = ProcessedImageField(verbose_name='Изображение для иконки',
                                     help_text="Высота изображения 100px | Формат PNG", upload_to='media/',
                                     format='PNG',
                                     options={'quality': 90},
                                     null=True, blank=True)
    avatarimage = ImageSpecField(source='icon_image',
                                 processors=[ResizeToFill(50, 50)],
                                 format='PNG',
                                 options={'quality': 50})
    svg = models.FileField("SVG - иконка", upload_to='uploads/', null=True)
    text=models.TextField(verbose_name='Текст элемента', help_text="Показывается под иконкой", max_length=3000, null = True, blank = True)
    group = models.IntegerField(verbose_name="Порядок следования на сайте", null=True, blank=True)


    class Meta:
        verbose_name = ('Блок | Регионы')
        verbose_name_plural = ('Блок | Регионы')

    def __str__(self):
        title = self.text[0:10] + "..."
        return u'%s' % title

class NewPriceBlock(models.Model):
    image=ProcessedImageField(verbose_name='Изображение для блока',help_text="Размер изображения не должен превышать 100кВ| Формат JPEG ", upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90},
                                           null = True, blank = True)
    image_webp = models.CharField(verbose_name='WEBP | Изображение для блока', max_length=600, null=True, blank=True)
    image_low = ImageSpecField(source='image',
                                 format='JPEG',
                                 options={'quality': 1})
    avatarimage = ImageSpecField(source='image',
                                 processors=[ResizeToFill(50, 50)],
                                 format='JPEG',
                                 options={'quality': 50})
    title = models.CharField('Заголовок блока', max_length=400, null=True, blank=True)
    text=models.TextField('Текст блока', max_length=1000, null=True, blank=True)
    price=models.CharField('Цена от..', max_length=400, null=True, blank=True)
    group = models.IntegerField(verbose_name="Порядок следования на сайте", null=True, blank=True)

    class Meta:
        verbose_name = ('Блок | Цены на католизаторы')
        verbose_name_plural = ('Блок | Цены на католизаторы')

    def __str__(self):
        return u'%s' % self.title

class NewPriceBlockInline(admin.TabularInline):
    model = NewPriceBlock

class NewPriceBlockAdmin(admin.ModelAdmin):
    list_display = ('title', '__str__', 'admin_thumbnail',)
    exclude = ('image_low', 'image_webp', )
    admin_thumbnail = AdminThumbnail(image_field='avatarimage')
    tabular=[NewPriceBlockInline]

class NewTextAbout(models.Model):
    text=RichTextUploadingField('Текст в первом абзаце', max_length=8000, null = True, blank = True)
    text_amp = RichTextUploadingField('Текст в первом абзаце|AMP - вариант', max_length=8000, null=True, blank=True)

    class Meta:
        verbose_name = ('Блок | О нас')
        verbose_name_plural = ('Блок | О нас')

    def __str__(self):
        self.title="Текст раздела"
        return u'%s' % self.title

@shared_task(acks_late=True)
def price_create_webp(pk):
    time.sleep(1.5)
    block = NewPriceBlock.objects.get(pk=pk)
    img_name = os.path.basename(block.image.url)
    webp_name = img_name.split('.')[0] + '.webp'
    img_path = media_path + img_name
    im = Image.open(img_path)
    im.save(media_path + webp_name, 'webp', quality='20')
    block.image_webp = '/media/media/' + webp_name
    block.save()

@receiver(post_save, sender= NewPriceBlock)
def priceblock_image(sender, instance, created, raw, using, **kwargs):
    if instance.image_webp and os.path.isfile('/usr/src/vekokat.ru/vekokat_ver2'+instance.image_webp):
        pass
    elif not instance.image:
        pass
    else:
        partners_create_webp(instance.pk)

class PartnersBlock(models.Model):
    title = models.CharField('Название партнера', max_length=1000, null=True, blank=True)
    city = models.CharField('Город расположения', max_length=1000, null=True, blank=True)
    image = ProcessedImageField(verbose_name='Логотип партнера', upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90},
                                           null = True, blank = True)
    image_low = ImageSpecField(source='image',
                                 format='JPEG',
                                 options={'quality': 1})
    image_webp = models.CharField(verbose_name='WEBP | Логотип партнера', max_length=600, null=True, blank=True)
    avatarimage = ImageSpecField(source='image',
                                 processors=[ResizeToFill(50, 50)],
                                 format='JPEG',
                                 options={'quality': 50})
    image_full = models.BooleanField("Изображение на вcю ширину блока", default= False)
    link = models.CharField('Ссылка на сайт партнера', max_length=1000, null=True, blank=True)
    text = RichTextUploadingField('Текст блока', max_length=5000, null=True, blank=True)

    class Meta:
        verbose_name = ('Блок | Партнер')
        verbose_name_plural = ('Блок | Партнеры')

    def __str__(self):
        return u'%s' % self.title

class PartnersBlockAdmin(admin.ModelAdmin):
    exclude = ('image_low', 'image_webp')

@shared_task(acks_late=True)
def partners_create_webp(pk):
    time.sleep(1.5)
    partner = PartnersBlock.objects.get(pk=pk)
    img_name = os.path.basename(partner.image.url)
    webp_name = img_name.split('.')[0] + '.webp'
    img_path = media_path + img_name
    im = Image.open(img_path)
    im.save(media_path + webp_name, 'webp', quality='20')
    partner.image_webp = '/media/media/' + webp_name
    partner.save()

@receiver(post_save, sender= PartnersBlock)
def partners_image(sender, instance, created, raw, using, **kwargs):
    if instance.image_webp and os.path.isfile('/usr/src/vekokat.ru/vekokat_ver2'+instance.image_webp):
        pass
    elif not instance.image:
        pass
    else:
        partners_create_webp(instance.pk)

class AdvantagesText(models.Model):
    text = RichTextUploadingField('Содержание', max_length=5000, null=True, blank=True)
    amp_text = RichTextUploadingField('AMP-вариант | Содержание', max_length=5000, null=True, blank=True)

    class Meta:
        verbose_name = ('Текст для блока ПРЕИУЩЕСТВА')
        verbose_name_plural = ('Текст для блока ПРЕИУЩЕСТВА')

    def __str__(self):
        self.title = "Текст"
        return u'%s' % self.title

class MethodsText(models.Model):
    text = RichTextUploadingField('Содержание', max_length=5000, null=True, blank=True)
    amp_text = RichTextUploadingField('AMP-вариант | Содержание', max_length=5000, null=True, blank=True)

    class Meta:
        verbose_name = ('Текст для блока ПОРЯДОК РАБОТЫ')
        verbose_name_plural = ('Текст для блока ПОРЯДОК РАБОТЫ')

    def __str__(self):
        self.title = "Текст"
        return u'%s' % self.title