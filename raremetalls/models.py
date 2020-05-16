# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PlatinumPrice(models.Model):
    price_rb=models.FloatField('Стоимость, рубли', null=True, blank=True,)
    price_dl = models.FloatField('Стоимость, доллар', null=True, blank=True,)
    price_eu = models.FloatField('Стоимость, евро', null=True, blank=True,)

    class Meta:
        verbose_name = ('Стоимость Платины')
        verbose_name_plural = ('Стоимость Платины')

    def __str__(self):
        self.title="Стоимость"
        return u'%s' % self.title

class TantalPrice(models.Model):
    price_rb=models.FloatField('Стоимость, рубли', null=True, blank=True,)
    price_dl = models.FloatField('Стоимость, доллар', null=True, blank=True,)
    price_eu = models.FloatField('Стоимость, евро', null=True, blank=True,)

    class Meta:
        verbose_name = ('Стоимость Палладия')
        verbose_name_plural = ('Стоимость Палладия')

    def __str__(self):
        self.title="Стоимость"
        return u'%s' % self.title

class RhodyiPrice(models.Model):
    price_rb=models.FloatField('Стоимость, рубли', null=True, blank=True,)
    price_dl = models.FloatField('Стоимость, доллар', null=True, blank=True,)
    price_eu = models.FloatField('Стоимость, евро', null=True, blank=True,)

    class Meta:
        verbose_name = ('Стоимость Родий')
        verbose_name_plural = ('Стоимость Родий')

    def __str__(self):
        self.title="Стоимость"
        return u'%s' % self.title
