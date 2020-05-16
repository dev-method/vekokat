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
send_mail('Запрос на обратную связь', "ПРОВЕРКА", 'admin@vekomet.ru', ['worker777@inbox.ru'],
                 fail_silently=False)

print ('excellent')
