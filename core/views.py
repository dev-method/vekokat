# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from core.serializers import AdvantagesSerializer, WorkingMethodsSerializer, LaboratorySerializer, RegionsSerializer, PriceBlockSerializer
from core.models import MainSeo
from core.models import NewSlider, NewAdvantages, NewWorkingMethods,NewLaboratory, NewRegions, NewPriceBlock, NewTextAbout, PartnersBlock
from core.models import AdvantagesText, MethodsText
from catalog.models import AutoCatalog
from django.http import HttpResponseRedirect
from orders.models import NewOrder
from vekokat_ver2.settings import DEBUG
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages

# Create your views here.

def mainpage_newdesign(request):
    adv_text = AdvantagesText.objects.all()
    met_text = MethodsText.objects.all()
    partners = PartnersBlock.objects.all()
    autocatalysts_rus = AutoCatalog.objects.all().filter(category_id=2)
    autocatalysts_foreign = AutoCatalog.objects.all().filter(category_id=1)
    seo=MainSeo.objects.all()
    debug_flag = DEBUG
    slides=NewSlider.objects.all()
    advantages=NewAdvantages.objects.all().order_by("group")
    methods=NewWorkingMethods.objects.all().order_by("group")
    laboratories=NewLaboratory.objects.all().order_by("group")
    regions=NewRegions.objects.all().order_by("group")
    price_blocks=NewPriceBlock.objects.all().order_by("group")
    about_text=NewTextAbout.objects.all()
    errors=[]
    form={}
    if request.POST:
        form['footer_phone'] = request.POST.get('footer_phone')
        form['name'] = request.POST.get('name')
        form['phone_mail'] = request.POST.get('phone_mail')
        form['phone_mail_modal'] = request.POST.get('phone_mail_modal')
        form['model'] = request.POST.get('model')
        form['valcat'] = request.POST.get('valcat')
        form['year'] = request.POST.get('year')
        form['typecat'] = request.POST.get('typecat')
        if not form['footer_phone'] and not form['phone_mail'] and not form['phone_mail_modal']:
            errors.append('- указать свой номер телефона|email')
        if not errors and request.recaptcha_is_valid:
            messages.add_message(request, messages.INFO, 'Ваша заявка отправлена, в ближайшее время с Вами свяжутся наши специалисты.')
            if form['phone_mail']:
                NewOrder.objects.create(name=form['name'], phone_mail=form['phone_mail'], model=form['model'],
                                        year=form['year'], valcat=form['valcat'], typecat=form['typecat'])
                return HttpResponseRedirect('/')
            elif form['footer_phone']:
                NewOrder.objects.create(name='', phone_mail=form['footer_phone'], model='',
                                        year='', valcat='', typecat='')
                return HttpResponseRedirect('/')
            elif form['phone_mail_modal']:
                NewOrder.objects.create(name=form['name'], phone_mail=form['phone_mail_modal'], model=form['model'],
                                        year=form['year'], valcat=form['valcat'], typecat=form['typecat'])
                return HttpResponseRedirect('/')
    if DEBUG:
        return render(request, 'core/dev/main-newdesign.html', {'seo':seo,'errors':errors, 'debug_flag':debug_flag, 'slides':slides, 'advantages':advantages, 'methods':methods, 'laboratories':laboratories,
                                                                'regions':regions, 'price_blocks':price_blocks, 'about_text':about_text, 'autocatalysts_rus': autocatalysts_rus, 'autocatalysts_foreign': autocatalysts_foreign,
                                                                'partners': partners, 'adv_text': adv_text, 'met_text': met_text})
    else:
        return render(request, 'core/prod/main-newdesign.html', {'seo':seo,'errors':errors,'debug_flag':debug_flag, 'slides':slides, 'advantages':advantages, 'methods':methods, 'laboratories':laboratories,
                                                                'regions':regions, 'price_blocks':price_blocks, 'about_text':about_text, 'autocatalysts_rus': autocatalysts_rus, 'autocatalysts_foreign': autocatalysts_foreign,
                                                                 'partners': partners,  'adv_text': adv_text, 'met_text': met_text})


def new_core_amp(request):
    seo = MainSeo.objects.all()
    adv_text = AdvantagesText.objects.all()
    met_text = MethodsText.objects.all()
    debug_flag = DEBUG
    slides = NewSlider.objects.all()
    partners = PartnersBlock.objects.all()
    autocatalysts_rus = AutoCatalog.objects.all().filter(category_id=2)
    autocatalysts_foreign = AutoCatalog.objects.all().filter(category_id=1)
    advantages = NewAdvantages.objects.all().order_by("group")
    methods = NewWorkingMethods.objects.all().order_by("group")
    laboratories = NewLaboratory.objects.all().order_by("group")
    regions = NewRegions.objects.all().order_by("group")
    price_blocks = NewPriceBlock.objects.all().order_by("group")
    about_text = NewTextAbout.objects.all()
    errors = []
    form = {}
    if request.POST:
        form['footer_phone'] = request.POST.get('footer_phone')
        form['name'] = request.POST.get('name')
        form['mail'] = request.POST.get('mail')
        form['phone'] = request.POST.get('phone')
        form['phone_modal'] = request.POST.get('phone_modal')
        if not form['footer_phone'] and not form['phone'] and not form['phone_modal']:
            errors.append('- указать свой номер телефона')
        if not errors:
            if form['phone']:
                NewOrder.objects.create(name=form['name'], mail=form['mail'], phone=form['phone'])
                return HttpResponseRedirect('/amp/')
            elif form['footer_phone']:
                NewOrder.objects.create(name=form['name'], mail=form['mail'], phone=form['footer_phone'])
                return HttpResponseRedirect('/amp/')
            elif form['phone_modal']:
                NewOrder.objects.create(name=form['name'], mail=form['mail'], phone=form['phone_modal'])
                return HttpResponseRedirect('/amp/')
    return render(request, 'core/amp/new-core-amp.html', {'errors':errors,'seo':seo, 'debug_flag':debug_flag, 'slides':slides, 'advantages':advantages, 'methods':methods, 'laboratories':laboratories,
                                                                'regions':regions, 'price_blocks':price_blocks, 'about_text':about_text, 'autocatalysts_rus': autocatalysts_rus, 'autocatalysts_foreign': autocatalysts_foreign,
                                                                'partners': partners, 'adv_text': adv_text, 'met_text': met_text})

def new_core_rss(request):
    seo = MainSeo.objects.all()
    met_text = MethodsText.objects.all()
    adv_text = AdvantagesText.objects.all()
    debug_flag = DEBUG
    slides = NewSlider.objects.all()
    partners = PartnersBlock.objects.all()
    autocatalysts_rus = AutoCatalog.objects.all().filter(category_id=2)
    autocatalysts_foreign = AutoCatalog.objects.all().filter(category_id=1)
    advantages = NewAdvantages.objects.all().order_by("group")
    methods = NewWorkingMethods.objects.all().order_by("group")
    laboratories = NewLaboratory.objects.all().order_by("group")
    regions = NewRegions.objects.all().order_by("group")
    price_blocks = NewPriceBlock.objects.all().order_by("group")
    about_text = NewTextAbout.objects.all()
    response = HttpResponse(content_type='text/rss')
    response['Content-Disposition'] = 'attachment;filename = "new-core-turbo.rss"'
    t = loader.get_template('core/yandex-turbo/new-core-turbo.rss')
    c = {'seo':seo, 'debug_flag':debug_flag, 'slides':slides, 'advantages':advantages, 'methods':methods, 'laboratories':laboratories,
                                                                'regions':regions, 'price_blocks':price_blocks, 'about_text':about_text,
                                                                'autocatalysts_rus': autocatalysts_rus, 'autocatalysts_foreign': autocatalysts_foreign,
                                                                'partners': partners, 'adv_text': adv_text, 'met_text': met_text}
    response.write(t.render(c))
    return response

@api_view(['GET'])
def advantages_api(request):
    if request.method == 'GET':
        advantages = NewAdvantages.objects.all()
        serializer = AdvantagesSerializer(advantages, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def working_methods_api(request):
    if request.method == 'GET':
        methods = NewWorkingMethods.objects.all()
        serializer = WorkingMethodsSerializer(methods, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def laboratory_api(request):
    if request.method == 'GET':
        laboratories = NewLaboratory.objects.all()
        serializer = LaboratorySerializer(laboratories, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def regions_api(request):
    if request.method == 'GET':
        regions = NewRegions.objects.all()
        serializer = RegionsSerializer(regions, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def price_blocks_api(request):
    if request.method == 'GET':
        blocks = NewPriceBlock.objects.all()
        serializer = PriceBlockSerializer(blocks, many=True)
        return Response(serializer.data)

def maintainance(request):
    return render(request, 'core/503.html')

def form_handler(request):
    errors=[]
    form={}
    if request.POST:
        form['post_url_footer'] = request.POST.get('post_url_footer')
        form['post_url_modal'] = request.POST.get('post_url_modal')
        form['post_url'] = request.POST.get('post_url')
        form['footer_phone'] = request.POST.get('footer_phone')
        form['name'] = request.POST.get('name')
        form['phone_mail'] = request.POST.get('phone_mail')
        form['phone_mail_modal'] = request.POST.get('phone_mail_modal')
        form['model'] = request.POST.get('model')
        form['valcat'] = request.POST.get('valcat')
        form['year'] = request.POST.get('year')
        form['typecat'] = request.POST.get('typecat')
        if not form['footer_phone'] and not form['phone_mail'] and not form['phone_mail_modal']:
            errors.append('- указать свой номер телефона|email')
            messages.add_message(request, messages.WARNING,
                                 '- необходимо указать свой номер телефона|email')
        if not errors and request.recaptcha_is_valid:
            messages.add_message(request, messages.INFO, 'Ваша заявка отправлена, в ближайшее время с Вами свяжутся наши специалисты.')
            if form['phone_mail']:
                NewOrder.objects.create(name=form['name'], phone_mail=form['phone_mail'], model=form['model'],
                                        year=form['year'], valcat=form['valcat'], typecat=form['typecat'])
                return HttpResponseRedirect(form['post_url'])
            elif form['footer_phone']:
                NewOrder.objects.create(name='', phone_mail=form['footer_phone'], model='',
                                        year='', valcat='', typecat='')
                return HttpResponseRedirect(form['post_url_footer'])
            elif form['phone_mail_modal']:
                NewOrder.objects.create(name=form['name'], phone_mail=form['phone_mail_modal'], model=form['model'],
                                        year=form['year'], valcat=form['valcat'], typecat=form['typecat'])
                return HttpResponseRedirect(form['post_url_modal'])
    return HttpResponseRedirect('/')

def form_amp_handler(request):
    errors = []
    form = {}
    if request.POST:
        form['post_url_footer'] = request.POST.get('post_url_footer')
        form['post_url_modal'] = request.POST.get('post_url_modal')
        form['post_url'] = request.POST.get('post_url')
        form['footer_phone'] = request.POST.get('footer_phone')
        form['name'] = request.POST.get('name')
        form['phone_mail'] = request.POST.get('phone_mail')
        form['phone_mail_modal'] = request.POST.get('phone_mail_modal')
        form['model'] = request.POST.get('model')
        form['valcat'] = request.POST.get('valcat')
        form['year'] = request.POST.get('year')
        form['typecat'] = request.POST.get('typecat')
        if not form['footer_phone'] and not form['phone_mail'] and not form['phone_mail_modal']:
            errors.append('- указать свой номер телефона|email')
        if not errors:
            if form['phone_mail']:
                NewOrder.objects.create(name=form['name'], phone_mail=form['phone_mail'], model=form['model'],
                                        year=form['year'], valcat=form['valcat'], typecat=form['typecat'])
                response = JsonResponse({"message":"Отправка формы прошла успешно"})
                response['AMP-Access-Control-Allow-Source-Origin'] = 'https://vekokat.ru'
                response['Access-Control-Expose-Headers'] = 'AMP-Access-Control-Allow-Source-Origin'
                return response
            elif form['footer_phone']:
                NewOrder.objects.create(name='', phone_mail=form['footer_phone'], model='',
                                        year='', valcat='', typecat='')
                response = JsonResponse({"message":"Отправка формы прошла успешно"})
                response['AMP-Access-Control-Allow-Source-Origin'] = 'https://vekokat.ru'
                response['Access-Control-Expose-Headers'] = 'AMP-Access-Control-Allow-Source-Origin'
                return response
            elif form['phone_mail_modal']:
                NewOrder.objects.create(name=form['name'], phone_mail=form['phone_mail_modal'], model=form['model'],
                                        year=form['year'], valcat=form['valcat'], typecat=form['typecat'])
                response = JsonResponse({"message":"Сообщение успешно отправлено!"})
                response['AMP-Access-Control-Allow-Source-Origin'] = 'https://vekokat.ru'
                response['Access-Control-Expose-Headers'] = 'AMP-Access-Control-Allow-Source-Origin'
                return response
    response = JsonResponse({"message":"Возникли проблемы с отправкой сообщения. Попробуйте еще раз."})
    response['AMP-Access-Control-Allow-Source-Origin'] = 'https://vekokat.ru'
    response['Access-Control-Expose-Headers'] = 'AMP-Access-Control-Allow-Source-Origin'
    return response

def form_rss_handler(request):
    errors = []
    form = {}
    if request.POST:
        form['post_url_footer'] = request.POST.get('post_url_footer')
        form['post_url_modal'] = request.POST.get('post_url_modal')
        form['post_url'] = request.POST.get('post_url')
        form['footer_phone'] = request.POST.get('footer_phone')
        form['name'] = request.POST.get('name')
        form['phone_mail'] = request.POST.get('phone_mail')
        form['phone_mail_modal'] = request.POST.get('phone_mail_modal')
        form['model'] = request.POST.get('model')
        form['valcat'] = request.POST.get('valcat')
        form['year'] = request.POST.get('year')
        form['typecat'] = request.POST.get('typecat')
        if not form['footer_phone'] and not form['phone_mail'] and not form['phone_mail_modal']:
            errors.append('- указать свой номер телефона|email')
        if not errors:
            if form['phone_mail']:
                NewOrder.objects.create(name=form['name'], phone_mail=form['phone_mail'], model=form['model'],
                                        year=form['year'], valcat=form['valcat'], typecat=form['typecat'])
                response = JsonResponse({"message":"Отправка формы прошла успешно"})
                response['AMP-Access-Control-Allow-Source-Origin'] = 'https://vekokat.ru'
                response['Access-Control-Expose-Headers'] = 'AMP-Access-Control-Allow-Source-Origin'
                return response
            elif form['footer_phone']:
                NewOrder.objects.create(name='', phone_mail=form['footer_phone'], model='',
                                        year='', valcat='', typecat='')
                response = JsonResponse({"message":"Отправка формы прошла успешно"})
                response['AMP-Access-Control-Allow-Source-Origin'] = 'https://vekokat.ru'
                response['Access-Control-Expose-Headers'] = 'AMP-Access-Control-Allow-Source-Origin'
                return response
            elif form['phone_mail_modal']:
                NewOrder.objects.create(name=form['name'], phone_mail=form['phone_mail_modal'], model=form['model'],
                                        year=form['year'], valcat=form['valcat'], typecat=form['typecat'])
                response = JsonResponse({"message":"Сообщение успешно отправлено!"})
                response['AMP-Access-Control-Allow-Source-Origin'] = 'https://vekokat.ru'
                response['Access-Control-Expose-Headers'] = 'AMP-Access-Control-Allow-Source-Origin'
                return response
    response = JsonResponse({"message":"Возникли проблемы с отправкой сообщения. Попробуйте еще раз."})
    response['AMP-Access-Control-Allow-Source-Origin'] = 'https://vekokat.ru'
    response['Access-Control-Expose-Headers'] = 'AMP-Access-Control-Allow-Source-Origin'
    return response

def map_intaractive(request):
    if DEBUG:
        return render(request, 'core/dev/map_interactive.html',{})
    else:
        return render(request, 'core/prod/map_interactive.html', {})

