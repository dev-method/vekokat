from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from core.models import NewPriceBlock
from catalog.serializers import AutoCatalogSerializer
from catalog.models import AutoCatalog, CatalyzatorCategory, CatalCatFoto
from vekokat_ver2.settings import DEBUG
# Create your views here.
@api_view(['GET'])
def catalog_api(request):
    if request.method == 'GET':
        catalog_item = AutoCatalog.objects.filter(category=2)
        serializer = AutoCatalogSerializer(catalog_item, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def foreign_catalog_api(request):
    if request.method == 'GET':
        catalog_item = AutoCatalog.objects.filter(category=1)
        serializer = AutoCatalogSerializer(catalog_item, many=True)
        return Response(serializer.data)

def otechcatalog_view(request):
    auto_models = AutoCatalog.objects.filter(cat_type_id=1)
    category = CatalyzatorCategory.objects.filter(id=1)
    if DEBUG:
        return render(request, 'catalog/dev/otech-catalog.html', {'auto_models': auto_models, 'category': category})
    else:
        return render(request, 'catalog/prod/otech-catalog.html', {'auto_models': auto_models, 'category': category})

def otechcatalog_amp(request):
    auto_models = AutoCatalog.objects.filter(cat_type_id=1)
    category = CatalyzatorCategory.objects.filter(id=1)
    return render(request, 'catalog/amp/otech-catalog-amp.html', {'auto_models': auto_models, 'category': category})


def otechcatalog_rss(request):
    auto_models = AutoCatalog.objects.filter(cat_type_id=1)
    category = CatalyzatorCategory.objects.filter(id=1)
    response = HttpResponse(content_type='text/rss')
    response['Content-Disposition'] = 'attachment;filename = "otechcatalog.rss"'
    t = loader.get_template('catalog/yandex-turbo/otechcatalog.rss')
    c = {'auto_models': auto_models, 'category': category}
    response.write(t.render(c))
    return response

def otechcatalog_item_view(request, slug):
    auto = AutoCatalog.objects.get(slug=slug)
    if DEBUG:
        return render(request, 'catalog/dev/otech-catalog-item.html', {'auto':auto})
    else:
        return render(request, 'catalog/prod/otech-catalog-item.html', {'auto':auto})

def otechcatalog_item_amp(request, slug):
    auto = AutoCatalog.objects.get(slug=slug)
    return render(request, 'catalog/amp/otech-catalog-item-amp.html', {'auto':auto})

def otechcatalog_item_rss(request):
    auto_models = AutoCatalog.objects.filter(cat_type_id=1)
    response = HttpResponse(content_type='text/rss')
    response['Content-Disposition'] = 'attachment;filename = "otechcatalog_item.rss"'
    t = loader.get_template('catalog/yandex-turbo/otechcatalog_item.rss')
    c = {'auto':auto_models}
    response.write(t.render(c))
    return response


def importcatalog_view(request):
    auto_models = AutoCatalog.objects.filter(cat_type=2)
    category = CatalyzatorCategory.objects.filter(id=2)
    if DEBUG:
        return render(request, 'catalog/dev/import-catalog.html', {'auto_models': auto_models, 'category': category})
    else:
        return render(request, 'catalog/prod/import-catalog.html', {'auto_models': auto_models, 'category': category})

def importcatalog_amp(request):
    auto_models = AutoCatalog.objects.filter(cat_type=2)
    category = CatalyzatorCategory.objects.filter(id=2)
    return render(request, 'catalog/amp/import-catalog-amp.html', {'auto_models': auto_models, 'category': category})

def importcatalog_rss(request):
    auto_models = AutoCatalog.objects.filter(cat_type=2)
    category = CatalyzatorCategory.objects.filter(id=2)
    response = HttpResponse(content_type='text/rss')
    response['Content-Disposition'] = 'attachment;filename = "importcatalog.rss"'
    t = loader.get_template('catalog/yandex-turbo/importcatalog.rss')
    c = {'auto_models': auto_models, 'category': category}
    response.write(t.render(c))
    return response

def importcatalog_item_view(request, slug):
    auto = AutoCatalog.objects.get(slug=slug)
    if DEBUG:
        return render(request, 'catalog/dev/import-catalog-item.html', {'auto':auto})
    else:
        return render(request, 'catalog/prod/import-catalog-item.html', {'auto':auto})

def importcatalog_item_amp(request, slug):
    auto = AutoCatalog.objects.get(slug=slug)
    return render(request, 'catalog/amp/import-catalog-item-amp.html', {'auto':auto})

def importcatalog_item_rss(request):
    auto_models = AutoCatalog.objects.filter(cat_type=2)
    response = HttpResponse(content_type='text/rss')
    response['Content-Disposition'] = 'attachment;filename = "importcatalog_item.rss"'
    t = loader.get_template('catalog/yandex-turbo/importcatalog_item.rss')
    c = {'auto':auto_models}
    response.write(t.render(c))
    return response


def catalizator_type_view(request, slug):
    cat_type = CatalyzatorCategory.objects.get(slug=slug)
    imgs = CatalCatFoto.objects.filter(position_id=cat_type.id)
    autocatalysts_rus = AutoCatalog.objects.all().filter(category_id=2)
    autocatalysts_foreign = AutoCatalog.objects.all().filter(category_id=1)
    price_blocks = NewPriceBlock.objects.all().order_by("group")
    if DEBUG:
        return render(request, 'catalog/dev/catalyzator-type.html', {'cat_type':cat_type, 'imgs': imgs, 'price_blocks':price_blocks,
                                                                     'autocatalysts_rus': autocatalysts_rus, 'autocatalysts_foreign': autocatalysts_foreign, 'open_gr_img': imgs[0]})
    else:
        return render(request, 'catalog/prod/catalyzator-type.html', {'cat_type':cat_type, 'imgs': imgs, 'price_blocks':price_blocks,
                                                                      'autocatalysts_rus': autocatalysts_rus, 'autocatalysts_foreign': autocatalysts_foreign, 'open_gr_img': imgs[0]})

def catalizator_type_amp(request, slug):
    cat_type = CatalyzatorCategory.objects.get(slug=slug)
    imgs = CatalCatFoto.objects.filter(position_id=cat_type.id)
    autocatalysts_rus = AutoCatalog.objects.all().filter(category_id=2)
    autocatalysts_foreign = AutoCatalog.objects.all().filter(category_id=1)
    price_blocks = NewPriceBlock.objects.all().order_by("group")
    return render(request, 'catalog/amp/catalyzator-type-amp.html', {'cat_type':cat_type, 'imgs': imgs, 'price_blocks':price_blocks,
                                                                      'autocatalysts_rus': autocatalysts_rus, 'autocatalysts_foreign': autocatalysts_foreign,})

def catal_otech_rss(request):
    cat_type = CatalyzatorCategory.objects.get(slug="otechestvennye-katalizatory")
    imgs = CatalCatFoto.objects.filter(position_id=cat_type.id)
    autocatalysts_rus = AutoCatalog.objects.all().filter(category_id=2)
    autocatalysts_foreign = AutoCatalog.objects.all().filter(category_id=1)
    price_blocks = NewPriceBlock.objects.all().order_by("group")
    response = HttpResponse(content_type='text/rss')
    response['Content-Disposition'] = 'attachment;filename = "catal_otech.rss"'
    t = loader.get_template('catalog/yandex-turbo/catal_type.rss')
    c = {'cat_type':cat_type, 'imgs': imgs, 'price_blocks':price_blocks,'autocatalysts_rus': autocatalysts_rus, 'autocatalysts_foreign': autocatalysts_foreign}
    response.write(t.render(c))
    return response

def catal_imort_rss(request):
    cat_type = CatalyzatorCategory.objects.get(slug="importnye-katalizatory")
    imgs = CatalCatFoto.objects.filter(position_id=cat_type.id)
    autocatalysts_rus = AutoCatalog.objects.all().filter(category_id=2)
    autocatalysts_foreign = AutoCatalog.objects.all().filter(category_id=1)
    price_blocks = NewPriceBlock.objects.all().order_by("group")
    response = HttpResponse(content_type='text/rss')
    response['Content-Disposition'] = 'attachment;filename = "catal_import.rss"'
    t = loader.get_template('catalog/yandex-turbo/catal_type.rss')
    c = {'cat_type':cat_type, 'imgs': imgs, 'price_blocks':price_blocks,'autocatalysts_rus': autocatalysts_rus, 'autocatalysts_foreign': autocatalysts_foreign}
    response.write(t.render(c))
    return response

def catal_metal_otech_rss(request):
    cat_type = CatalyzatorCategory.objects.get(slug="otechestvennye-metallicheskie-katalizatory")
    imgs = CatalCatFoto.objects.filter(position_id=cat_type.id)
    autocatalysts_rus = AutoCatalog.objects.all().filter(category_id=2)
    autocatalysts_foreign = AutoCatalog.objects.all().filter(category_id=1)
    price_blocks = NewPriceBlock.objects.all().order_by("group")
    response = HttpResponse(content_type='text/rss')
    response['Content-Disposition'] = 'attachment;filename = "catal_metal_otech.rss"'
    t = loader.get_template('catalog/yandex-turbo/catal_type.rss')
    c = {'cat_type':cat_type, 'imgs': imgs, 'price_blocks':price_blocks,'autocatalysts_rus': autocatalysts_rus, 'autocatalysts_foreign': autocatalysts_foreign}
    response.write(t.render(c))
    return response

def catal_metal_import_rss(request):
    cat_type = CatalyzatorCategory.objects.get(slug="importnye-metallicheskie-katalizatory")
    imgs = CatalCatFoto.objects.filter(position_id=cat_type.id)
    autocatalysts_rus = AutoCatalog.objects.all().filter(category_id=2)
    autocatalysts_foreign = AutoCatalog.objects.all().filter(category_id=1)
    price_blocks = NewPriceBlock.objects.all().order_by("group")
    response = HttpResponse(content_type='text/rss')
    response['Content-Disposition'] = 'attachment;filename = "catal_metal_import.rss"'
    t = loader.get_template('catalog/yandex-turbo/catal_type.rss')
    c = {'cat_type':cat_type, 'imgs': imgs, 'price_blocks':price_blocks,'autocatalysts_rus': autocatalysts_rus, 'autocatalysts_foreign': autocatalysts_foreign}
    response.write(t.render(c))
    return response

def sazhev_rss(request):
    cat_type = CatalyzatorCategory.objects.get(slug="sazhevye-filtry")
    imgs = CatalCatFoto.objects.filter(position_id=cat_type.id)
    autocatalysts_rus = AutoCatalog.objects.all().filter(category_id=2)
    autocatalysts_foreign = AutoCatalog.objects.all().filter(category_id=1)
    price_blocks = NewPriceBlock.objects.all().order_by("group")
    response = HttpResponse(content_type='text/rss')
    response['Content-Disposition'] = 'attachment;filename = "sazhev.rss"'
    t = loader.get_template('catalog/yandex-turbo/catal_type.rss')
    c = {'cat_type':cat_type, 'imgs': imgs, 'price_blocks':price_blocks,'autocatalysts_rus': autocatalysts_rus, 'autocatalysts_foreign': autocatalysts_foreign}
    response.write(t.render(c))
    return response