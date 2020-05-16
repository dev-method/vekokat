# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, '/usr/src/vekokat.ru/vekokat_ver2')
sys.path.append('/usr/src/vekokat.ru/vekokat_ver2')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'vekokat_ver2.settings')
import django
django.setup()
from django.core.mail import send_mail

from orders.models import Order, ServiceOrder, NewOrder
mess=ServiceOrder.objects.all()
neworders=NewOrder.objects.filter(save_order=False)

try:
   for item in neworders:
       subject = "Имя:  "+item.name+"\n" + "Телефон или почта:  "+item.phone_mail+"\n"+"Марка|модель автомобиля:  " + item.model + "\n"+"Год выпуска:  "+item.year+ "\n" + "Объем|тип мотора:  "+item.valcat + "\n" + "Тип катализатора:  "+item.typecat
       send_mail('Запрос на обратную связь', subject, 'admin@vekomet.ru', ['worker777@inbox.ru'],
                 fail_silently=False)
       item.save_order=True
       item.save()
except NewOrder.DoesNotExist:
    pass

try:
   for m in mess:
       subjname=m.name
       subjcontacts=m.contacts
       subjdesc=m.description
       subject="От:   "+subjname+"    Контакты:   "+subjcontacts+"     Описание:     "+subjdesc
       send_mail('Заявка', subject, 'admin@vekomet.ru',['worker777@inbox.ru'], fail_silently=False)
       name=m.name
       contacts=m.contacts
       desc=m.description
       n=Order.objects.create(name=name, contacts=contacts, description=desc)
       n.save()
       m.delete()
except ServiceOrder.DoesNotExist:
    pass

print ('excellent')
