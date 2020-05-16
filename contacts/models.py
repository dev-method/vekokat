# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class ContactsText(models.Model):
    sub=RichTextField('Текст', max_length=6000)

    class Meta:
        verbose_name = ('ТЕКСТ НА СТР КОНТАКТЫ')
        verbose_name_plural = ('ТЕКСТЫ НА СТР КОНТАКТЫ')

    def __unicode__(self):
        self.title="Текс на стр Контакты"
        return u'%s' % self.title

class ContactsSeo(models.Model):
    title=models.TextField('title', max_length=300, null=True,blank=True)
    description=models.TextField('description', max_length=1000, null=True,blank=True)
    keywords=models.TextField('keywords', max_length=1000, null=True,blank=True)

    class Meta:
        verbose_name = ('SEO')
        verbose_name_plural = ('SEO')

    def __unicode__(self):
        self.title="SEO"
        return u'%s' % self.title