from django.db import models
from django.contrib import admin
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from PIL import Image
import os, time
from celery import shared_task
from django.db.models.signals import post_save
from django.dispatch import receiver

media_path = '/usr/src/vekokat.ru/vekokat_ver2/media/media/'
app_url = '/usr/src/vekokat.ru/vekokat_ver2'

# Create your models here.

class City(models.Model):
    seotitle = models.CharField('Seo-title', null=True, blank=True, max_length=300)
    seodescript = models.CharField('Seo-description', null=True, blank=True, max_length=3000)
    seokeywords = models.CharField('Seo-keywords', null=True, blank=True, max_length=3000)
    slug = models.SlugField(blank=True, null=True)
    city_name = models.CharField('Название города', max_length=1000, null=True, blank=True)
    image_1=ProcessedImageField(verbose_name='№1 | 1920px | Изображение города',upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90},null=True,
                                    blank=True)
    image_1_low = ImageSpecField(source='image_1',
                                 format='JPEG',
                                 options={'quality': 1})
    image_1_webp = models.CharField(verbose_name='WEBP | №1 | 1920px | Изображение города', max_length=600, null=True, blank=True)
    image_1_jp2 = models.CharField(verbose_name='JPEG2000 | №1 | 1920px | Изображение города', max_length=600, null=True, blank=True)

    image_1_768 = ProcessedImageField(verbose_name='№1 | 768px | Изображение города', upload_to='media/',
                                  format='JPEG',
                                  options={'quality': 90},null=True,
                                    blank=True)
    image_1_768_low = ImageSpecField(source='image_1_768',
                                 format='JPEG',
                                 options={'quality': 1})
    image_1_768_webp = models.CharField(verbose_name='WEBP | №1 | 768px | Изображение города', max_length=600, null=True, blank=True)
    image_1_768_jp2 = models.CharField(verbose_name='JPEG2000 | №1 | 768px | Изображение города', max_length=600, null=True, blank=True)
    image_1_576 = ProcessedImageField(verbose_name='№1 | 576px | Изображение города', upload_to='media/',
                                      format='JPEG',
                                      options={'quality': 90},null=True,
                                    blank=True)
    image_1_576_low = ImageSpecField(source='image_1_576',
                                     format='JPEG',
                                     options={'quality': 1})
    image_1_576_webp = models.CharField(verbose_name='WEBP | №1 | 576px | Изображение города', max_length=600, null=True, blank=True)
    image_1_576_jp2 = models.CharField(verbose_name='JPEG2000 | №1 | 576px | Изображение города', max_length=600, null=True, blank=True)
    image_2 = ProcessedImageField(verbose_name='№2 | 1920px | Изображение города', upload_to='media/',
                                  format='JPEG',
                                  options={'quality': 90},null=True,
                                    blank=True)
    image_2_low = ImageSpecField(source='image_2',
                                 format='JPEG',
                                 options={'quality': 1})
    image_2_webp = models.CharField(verbose_name='WEBP | №2 | 1920px | Изображение города', max_length=600, null=True,
                                    blank=True)
    image_2_jp2 = models.CharField(verbose_name='JPEG2000 | №2 | 1920px | Изображение города', max_length=600, null=True,
                                    blank=True)

    image_2_768 = ProcessedImageField(verbose_name='№2 | 768px | Изображение города', upload_to='media/',
                                      format='JPEG',
                                      options={'quality': 90},null=True,
                                    blank=True)
    image_2_768_low = ImageSpecField(source='image_2_768',
                                     format='JPEG',
                                     options={'quality': 1})
    image_2_768_webp = models.CharField(verbose_name='WEBP | №2 | 768px | Изображение города', max_length=600,
                                        null=True, blank=True)
    image_2_768_jp2 = models.CharField(verbose_name='JPEG2000 | №2 | 768px | Изображение города', max_length=600,
                                        null=True, blank=True)
    image_2_576 = ProcessedImageField(verbose_name='№2 | 576px | Изображение города', upload_to='media/',
                                      format='JPEG',
                                      options={'quality': 90},null=True,
                                    blank=True)
    image_2_576_low = ImageSpecField(source='image_2_576',
                                     format='JPEG',
                                     options={'quality': 1})
    image_2_576_webp = models.CharField(verbose_name='WEBP | №2 | 576px | Изображение города', max_length=600,
                                        null=True, blank=True)
    image_2_576_jp2 = models.CharField(verbose_name='JPEG2000 | №2 | 576px | Изображение города', max_length=600,
                                        null=True, blank=True)
    image_3 = ProcessedImageField(verbose_name='№3 | 1920px | Изображение города', upload_to='media/',
                                  format='JPEG',
                                  options={'quality': 90},null=True,
                                    blank=True)
    image_3_low = ImageSpecField(source='image_3',
                                 format='JPEG',
                                 options={'quality': 1})
    image_3_webp = models.CharField(verbose_name='WEBP | №3 | 1920px | Изображение города', max_length=600, null=True,
                                    blank=True)
    image_3_jp2 = models.CharField(verbose_name='WEBP | №3 | 1920px | Изображение города', max_length=600, null=True,
                                    blank=True)
    image_3_768 = ProcessedImageField(verbose_name='№3 | 768px | Изображение города', upload_to='media/',
                                      format='JPEG',
                                      options={'quality': 90},null=True,
                                    blank=True)
    image_3_768_low = ImageSpecField(source='image_3_768',
                                     format='JPEG',
                                     options={'quality': 1})
    image_3_768_webp = models.CharField(verbose_name='WEBP | №3 | 768px | Изображение города', max_length=600,
                                        null=True, blank=True)
    image_3_768_jp2 = models.CharField(verbose_name='JPEG2000 | №3 | 768px | Изображение города', max_length=600,
                                        null=True, blank=True)
    image_3_576 = ProcessedImageField(verbose_name='№3 | 576px | Изображение города', upload_to='media/',
                                      format='JPEG',
                                      options={'quality': 90},null=True,
                                    blank=True)
    image_3_576_low = ImageSpecField(source='image_3_576',
                                     format='JPEG',
                                     options={'quality': 1})
    image_3_576_webp = models.CharField(verbose_name='WEBP | №3 | 576px | Изображение города', max_length=600,
                                        null=True, blank=True)
    image_3_576_jp2 = models.CharField(verbose_name='JPEG2000 | №3 | 576px | Изображение города', max_length=600,
                                        null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


    class Meta:
        verbose_name = ('СТРАНИЦА ГОРОДА')
        verbose_name_plural = ('СТРАНИЦЫ ГОРОДОВ')

    def __str__(self):
        return u'%s' % self.city_name

    def get_absolute_url(self):
        return "/priem-katalizatorov/%s/" % self.slug

class CityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['city_name', 'slug']}),
        ('SEO', {'fields': ['seotitle', 'seodescript', 'seokeywords'],
                 'classes': ['collapse']}),
        ('Фото для слайдера №1', {'fields': ['image_1', 'image_1_768', 'image_1_576'], 'classes': ['collapse']}),
        ('Фото для слайдера №2', {'fields': ['image_2', 'image_2_768', 'image_2_576'], 'classes': ['collapse']}),
        ('Фото для слайдера №3', {'fields': ['image_3', 'image_3_768', 'image_3_576'], 'classes': ['collapse']}),
    ]

@shared_task(acks_late=True)
def cities_alter_formats(pk):
    time.sleep(1)
    catalog_item = City.objects.get(pk=pk)
    origin_name_1 = os.path.basename(catalog_item.image_1.url)
    origin_name_1_768 = os.path.basename(catalog_item.image_1_768.url)
    origin_name_1_576 = os.path.basename(catalog_item.image_1_576.url)
    origin_name_2 = os.path.basename(catalog_item.image_2.url)
    origin_name_2_768 = os.path.basename(catalog_item.image_2_768.url)
    origin_name_2_576 = os.path.basename(catalog_item.image_2_576.url)
    origin_name_3 = os.path.basename(catalog_item.image_3.url)
    origin_name_3_768 = os.path.basename(catalog_item.image_3_768.url)
    origin_name_3_576 = os.path.basename(catalog_item.image_3_576.url)
    clear_name_1 = origin_name_1.split('.')[0]
    clear_name_1_768 = origin_name_1_768.split('.')[0]
    clear_name_1_576 = origin_name_1_576.split('.')[0]
    clear_name_2 = origin_name_2.split('.')[0]
    clear_name_2_768 = origin_name_2_768.split('.')[0]
    clear_name_2_576 = origin_name_2_576.split('.')[0]
    clear_name_3 = origin_name_3.split('.')[0]
    clear_name_3_768 = origin_name_3_768.split('.')[0]
    clear_name_3_576 = origin_name_3_576.split('.')[0]
    Image.open(media_path + origin_name_1).save(media_path + clear_name_1 + '.webp', 'webp', quality='70')
    Image.open(media_path + origin_name_1).save(media_path + clear_name_1 + '.jpx', 'JPEG2000', quality_mode='dB',
                                              quality_layers=[34])
    Image.open(media_path + origin_name_1_768).save(media_path + clear_name_1_768 + '.webp', 'webp', quality='70')
    Image.open(media_path + origin_name_1_768).save(media_path + clear_name_1_768 + '.jpx', 'JPEG2000', quality_mode='dB',
                                                quality_layers=[34])
    Image.open(media_path + origin_name_1_576).save(media_path + clear_name_1_576 + '.webp', 'webp', quality='70')
    Image.open(media_path + origin_name_1_576).save(media_path + clear_name_1_576 + '.jpx', 'JPEG2000', quality_mode='dB',
                                                quality_layers=[34])
    Image.open(media_path + origin_name_2).save(media_path + clear_name_2 + '.webp', 'webp', quality='70')
    Image.open(media_path + origin_name_2).save(media_path + clear_name_2 + '.jpx', 'JPEG2000', quality_mode='dB',
                                                quality_layers=[34])
    Image.open(media_path + origin_name_2_768).save(media_path + clear_name_2_768 + '.webp', 'webp', quality='70')
    Image.open(media_path + origin_name_2_768).save(media_path + clear_name_2_768 + '.jpx', 'JPEG2000',
                                                    quality_mode='dB',
                                                    quality_layers=[34])
    Image.open(media_path + origin_name_2_576).save(media_path + clear_name_2_576 + '.webp', 'webp', quality='70')
    Image.open(media_path + origin_name_2_576).save(media_path + clear_name_2_576 + '.jpx', 'JPEG2000',
                                                    quality_mode='dB',
                                                    quality_layers=[34])
    Image.open(media_path + origin_name_3).save(media_path + clear_name_3 + '.webp', 'webp', quality='70')
    Image.open(media_path + origin_name_3).save(media_path + clear_name_3 + '.jpx', 'JPEG2000', quality_mode='dB',
                                                quality_layers=[34])
    Image.open(media_path + origin_name_3_768).save(media_path + clear_name_3_768 + '.webp', 'webp', quality='70')
    Image.open(media_path + origin_name_3_768).save(media_path + clear_name_3_768 + '.jpx', 'JPEG2000',
                                                    quality_mode='dB',
                                                    quality_layers=[34])
    Image.open(media_path + origin_name_3_576).save(media_path + clear_name_3_576 + '.webp', 'webp', quality='70')
    Image.open(media_path + origin_name_3_576).save(media_path + clear_name_3_576 + '.jpx', 'JPEG2000',
                                                    quality_mode='dB',
                                                    quality_layers=[34])

    catalog_item.image_1_webp = '/media/media/' + clear_name_1+'.webp'
    catalog_item.image_1_jp2 = '/media/media/' + clear_name_1 + '.jpx'
    catalog_item.image_1_768_webp = '/media/media/' + clear_name_1_768 + '.webp'
    catalog_item.image_1_768_jp2 = '/media/media/' + clear_name_1_768 + '.jpx'
    catalog_item.image_1_576_webp = '/media/media/' + clear_name_1_576 + '.webp'
    catalog_item.image_1_576_jp2 = '/media/media/' + clear_name_1_576 + '.jpx'
    catalog_item.image_2_webp = '/media/media/' + clear_name_2 + '.webp'
    catalog_item.image_2_jp2 = '/media/media/' + clear_name_2 + '.jpx'
    catalog_item.image_2_768_webp = '/media/media/' + clear_name_2_768 + '.webp'
    catalog_item.image_2_768_jp2 = '/media/media/' + clear_name_2_768 + '.jpx'
    catalog_item.image_2_576_webp = '/media/media/' + clear_name_2_576 + '.webp'
    catalog_item.image_2_576_jp2 = '/media/media/' + clear_name_2_576 + '.jpx'
    catalog_item.image_3_webp = '/media/media/' + clear_name_3 + '.webp'
    catalog_item.image_3_jp2 = '/media/media/' + clear_name_3 + '.jpx'
    catalog_item.image_3_768_webp = '/media/media/' + clear_name_3_768 + '.webp'
    catalog_item.image_3_768_jp2 = '/media/media/' + clear_name_3_768 + '.jpx'
    catalog_item.image_3_576_webp = '/media/media/' + clear_name_3_576 + '.webp'
    catalog_item.image_3_576_jp2 = '/media/media/' + clear_name_3_576 + '.jpx'
    catalog_item.save()

@receiver(post_save, sender= City)
def methods_image(sender, instance, created, raw, using, **kwargs):
    if instance.image_1_webp and instance.image_1_jp2:
        if not os.path.isfile(app_url+instance.image_1_webp):
            cities_alter_formats(instance.pk)
        elif not os.path.isfile(app_url+instance.image_1_jp2):
            cities_alter_formats(instance.pk)
        else:
            pass
    elif instance.image_1:
        cities_alter_formats(instance.pk)
    else:
        pass