# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from contacts.models import ContactsText, ContactsSeo
from orders.models import ServiceOrder, NewOrder
from vekokat_ver2.settings import DEBUG
from django.contrib import messages

def new_contacts(request):
    debug_flag = DEBUG
    seo=ContactsSeo.objects.all()
    texts=ContactsText.objects.all()
    errors = []
    form = {}
    if request.POST:
        form['contacts_name'] = request.POST.get('contacts_name')
        form['contacts_contacts'] = request.POST.get('contacts_contacts')
        form['description'] = request.POST.get('description')
        form['name'] = request.POST.get('name')
        form['footer_phone'] = request.POST.get('footer_phone')
        form['phone_mail'] = request.POST.get('phone_mail')
        form['phone_mail_modal'] = request.POST.get('phone_mail_modal')
        form['model'] = request.POST.get('model')
        form['valcat'] = request.POST.get('valcat')
        form['year'] = request.POST.get('year')
        form['typecat'] = request.POST.get('typecat')
        if not form['footer_phone'] and not form['phone_mail'] and not form['contacts_contacts']:
            errors.append('- указать свой номер телефона или почту')
        if not errors and request.recaptcha_is_valid:
            messages.add_message(request, messages.INFO,
                                 'Ваша заявка отправлена, в ближайшее время с Вами свяжутся наши специалисты.')
            if form['phone_mail']:
                NewOrder.objects.create(name=form['name'], phone_mail=form['phone_mail'], model=form['model'],
                                        year=form['year'], valcat=form['valcat'], typecat=form['typecat'])
                return HttpResponseRedirect('/contacts/')
            elif form['footer_phone']:
                NewOrder.objects.create(name='', phone_mail=form['footer_phone'], model='',
                                        year='', valcat='', typecat='')
                return HttpResponseRedirect('/contacts/')
            elif form['phone_mail_modal']:
                NewOrder.objects.create(name=form['name'], phone_mail=form['phone_mail_modal'], model=form['model'],
                                        year=form['year'], valcat=form['valcat'], typecat=form['typecat'])
                return HttpResponseRedirect('/contacts/')
            elif form['contacts_contacts']:
                ServiceOrder.objects.create(name=form['contacts_name'], contacts=form['contacts_contacts'], description=form['description'])
                return HttpResponseRedirect('/contacts/')
    if DEBUG:
        return render(request, 'contacts/dev/new-contacts.html', {'debug_flag':debug_flag, 'seo':seo, 'texts':texts, 'errors':errors})
    else:
        return render(request, 'contacts/prod/new-contacts.html', {'debug_flag':debug_flag, 'seo': seo, 'texts': texts, 'errors': errors})

def new_contacts_amp(request):
    debug_flag = DEBUG
    seo=ContactsSeo.objects.all()
    texts=ContactsText.objects.all()
    errors = []
    form = {}
    if request.POST:
        form['contacts_name'] = request.POST.get('contacts_name')
        form['contacts_contacts'] = request.POST.get('contacts_contacts')
        form['description'] = request.POST.get('description')
        form['footer_phone'] = request.POST.get('footer_phone')
        form['name'] = request.POST.get('name')
        form['mail'] = request.POST.get('mail')
        form['phone'] = request.POST.get('phone')
        form['phone_modal'] = request.POST.get('phone_modal')
        if not form['footer_phone'] and not form['phone'] and not form['contacts_contacts']:
            errors.append('- указать свой номер телефона или почту')
        if not errors:
            if form['phone']:
                order = NewOrder.objects.create(name=form['name'], mail=form['mail'], phone=form['phone'])
                order.save()
                return HttpResponseRedirect('/amp/contacts/')
            elif form['footer_phone']:
                order = NewOrder.objects.create(name=form['name'], mail=form['mail'], phone=form['footer_phone'])
                order.save()
                return HttpResponseRedirect('/amp/contacts/')
            elif form['phone_modal']:
                order = NewOrder.objects.create(name=form['name'], mail=form['mail'], phone=form['phone_modal'])
                order.save()
                return HttpResponseRedirect('/amp/contacts/')
            elif form['contacts_contacts']:
                order = ServiceOrder.objects.create(name=form['contacts_name'], contacts=form['contacts_contacts'], description=form['description'])
                order.save()
                return HttpResponseRedirect('/amp/contacts/')
    if DEBUG:
        return render(request, 'contacts/amp/new-contacts-amp.html', {'debug_flag':debug_flag, 'seo':seo, 'texts':texts, 'errors':errors})
    else:
        return render(request, 'contacts/amp/prod/new-contacts-amp.html', {'debug_flag':debug_flag, 'seo': seo, 'texts': texts, 'errors': errors})
