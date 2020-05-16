from django.db import models
from django.contrib import admin
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
import os, time
from celery import shared_task
from django.db.models.signals import post_save
from django.dispatch import receiver

media_path = '/usr/src/vekokat.ru/vekokat_ver2/media/media/'
app_url = '/usr/src/vekokat.ru/vekokat_ver2'

# Create your models here.
class ConditionsSeo(models.Model):
    title=models.TextField('title', max_length=300, null=True,blank=True)
    description=models.TextField('description', max_length=1000, null=True,blank=True)
    keywords=models.TextField('keywords', max_length=1000, null=True,blank=True)

    class Meta:
        verbose_name = ('SEO')
        verbose_name_plural = ('SEO')

    def __str__(self):
        self.title="SEO"
        return u'%s' % self.title


class Conditions(models.Model):
    image = ProcessedImageField(verbose_name='Изображение для баннера', upload_to='media/',
                                format='JPEG',
                                options={'quality': 90},
                                null=True, blank=True)
    image_low = ImageSpecField(source='image',
                               format='JPEG',
                               options={'quality': 1})
    image_webp = models.CharField(verbose_name='WEBP | Изображение для баннера', max_length=600, null=True, blank=True)
    image_jp2 = models.CharField(verbose_name='JPEG2000 | Изображение для баннера', max_length=600, null=True, blank=True)
    text_part1 = RichTextUploadingField('Текст| Часть1', null=True, blank=True)
    text_part1_amp = RichTextUploadingField('Текст - AMP- вариант| Часть1', null=True, blank=True)
    text_part2 = RichTextUploadingField('Текст| Часть2', null=True, blank=True)
    text_part2_amp = RichTextUploadingField('Текст - AMP- вариант| Часть2', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = ('ТЕКСТ К УСЛОВИЯМ ПРИЕМА')
        verbose_name_plural = ('ТЕКСТА К УСЛОВИЯМ ПРИЕМА')

    def __str__(self):
        self.title = "Содержание"
        return u'%s' % self.title

class ConditionsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['image', 'image_webp', 'text_part1', 'text_part2']}),
        ('AMP', {'fields': ['text_part1_amp', 'text_part2_amp'],
                 'classes': ['collapse']})
    ]

@shared_task(acks_late=True)
def conditions_alter_formats(pk):
    time.sleep(1.5)
    catalog_item = Conditions.objects.get(pk=pk)
    origin_name = os.path.basename(catalog_item.image.url)
    clear_name = origin_name.split('.')[0]
    Image.open(media_path+origin_name).save(media_path+clear_name+'.webp', 'webp', quality='70')
    Image.open(media_path + origin_name).save(media_path + clear_name + '.jpx', 'JPEG2000', quality_mode='dB', quality_layers=[34])
    catalog_item.image_webp = '/media/media/' + clear_name+'.webp'
    catalog_item.image_jp2 = '/media/media/' + clear_name + '.jpx'
    catalog_item.save()

@receiver(post_save, sender= Conditions)
def methods_image(sender, instance, created, raw, using, **kwargs):
    if instance.image_webp and instance.image_jp2:
        if not os.path.isfile(app_url+instance.image_webp):
            conditions_alter_formats(instance.pk)
        elif not os.path.isfile(app_url+instance.image_jp2):
            conditions_alter_formats(instance.pk)
        else:
            pass
    elif instance.image:
        conditions_alter_formats(instance.pk)
    else:
        pass