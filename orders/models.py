# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from orders.send_order_tasks import send_order
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models



# Create your models here.
class Order(models.Model):
    name=models.CharField('Имя клиента', max_length=200)
    contacts=models.CharField('Контактные данные', max_length=600)
    description=models.TextField('Запрос',max_length=4000 )

    class Meta:
        verbose_name = ('Заявка')
        verbose_name_plural = ('Заявки')

    def __str__(self):
        return u'%s' % self.name

class ServiceOrder(models.Model):
    name=models.CharField('Имя клиента', max_length=200)
    contacts=models.CharField('Контактные данные', max_length=600)
    description=models.TextField('Запрос',max_length=4000 )

    class Meta:
        verbose_name = ('Сервисная Заявка')
        verbose_name_plural = ('Сервисные Заявки')

    def __str__(self):
        return u'%s' % self.name

class NewOrder(models.Model):
    name=models.CharField('Имя клиента', help_text="Необязательный параметр", max_length=200, null=True, blank=True)
    phone_mail = models.CharField('Почта или телефон клиента', help_text="Обязательный параметр", max_length=600,
                                  null=True, blank=True)
    model = models.CharField('Марка|модель автомобиля', help_text="Необязательный параметр", max_length=1000, null=True, blank=True)
    year = models.CharField('Год выпуска', help_text="Необязательный параметр", max_length=500, null=True, blank=True)
    valcat = models.CharField('Объем|тип мотора (дизель|бензин)', help_text="Необязательный параметр", max_length=1200, null=True, blank=True)
    typecat = models.CharField('Тип катализатора (керамика|металл)', help_text="Необязательный параметр", max_length=1000, null=True, blank=True)
    save_order = models.BooleanField(default=False)

    class Meta:
        verbose_name = ('Запрос на обратную связь')
        verbose_name_plural = ('Запросы на обратную связь')

    def __str__(self):
        return u'%s' % self.name

@receiver(post_save, sender=NewOrder)
def new_order_sendmail(sender, instance, created, raw, using, **kwargs):
    send_order(instance.name, instance.phone_mail, instance.model, instance.year, instance.valcat, instance.typecat)



class NewServiceOrder(models.Model):
    name=models.CharField('Имя клиента', help_text="Необязательный параметр", max_length=200, null=True, blank=True)
    mail = models.CharField('Почта клиента', help_text="Необязательный параметр", max_length=600, null=True, blank=True)
    phone = models.CharField('Телефон клиента', max_length=600)


    class Meta:
        verbose_name = ('Запрос на обратную связь')
        verbose_name_plural = ('Запросы на обратную связь')

    def __str__(self):
        return u'%s' % self.name

