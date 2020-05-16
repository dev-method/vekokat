from django.shortcuts import render
from cities.models import City
from django.http import HttpResponse
from django.template import loader
from core.models import NewWorkingMethods, NewPriceBlock
from catalog.models import AutoCatalog
from vekokat_ver2.settings import DEBUG

# Create your views here.

def city_view(request, slug):
    full_width = "width-modificator"
    autocatalysts_rus = AutoCatalog.objects.all().filter(category_id=2)
    autocatalysts_foreign = AutoCatalog.objects.all().filter(category_id=1)
    methods = NewWorkingMethods.objects.all().order_by("group")
    price_blocks = NewPriceBlock.objects.all().order_by("group")
    city = City.objects.get(slug=slug)
    if DEBUG:
        return render(request, 'cities/dev/cities.html', {'full_width':full_width, 'city': city, 'autocatalysts_rus': autocatalysts_rus, 'price_blocks':price_blocks,
                                                          'autocatalysts_foreign': autocatalysts_foreign, 'methods':methods,})
    else:
        return render(request, 'cities/prod/cities.html', {'full_width':full_width, 'city': city, 'autocatalysts_rus': autocatalysts_rus, 'price_blocks':price_blocks,
                                                           'autocatalysts_foreign': autocatalysts_foreign, 'methods':methods,})

def amp_city_view(request, slug):
    full_width = "width-modificator"
    autocatalysts_rus = AutoCatalog.objects.all().filter(category_id=2)
    autocatalysts_foreign = AutoCatalog.objects.all().filter(category_id=1)
    methods = NewWorkingMethods.objects.all().order_by("group")
    price_blocks = NewPriceBlock.objects.all().order_by("group")
    city = City.objects.get(slug=slug)
    return render(request, 'cities/amp/cities-amp.html', {'full_width':full_width, 'city': city, 'autocatalysts_rus': autocatalysts_rus, 'price_blocks':price_blocks,
                                                           'autocatalysts_foreign': autocatalysts_foreign, 'methods':methods,})

def cities_rss(request):
    autocatalysts_rus = AutoCatalog.objects.all().filter(category_id=2)
    autocatalysts_foreign = AutoCatalog.objects.all().filter(category_id=1)
    methods = NewWorkingMethods.objects.all().order_by("group")
    price_blocks = NewPriceBlock.objects.all().order_by("group")
    cities = City.objects.all()
    response = HttpResponse(content_type='text/rss')
    response['Content-Disposition'] = 'attachment;filename = "cities.rss"'
    t = loader.get_template('cities/yandex-turbo/cities-turbo.rss')
    c = {'autocatalysts_rus': autocatalysts_rus, 'price_blocks':price_blocks,
         'autocatalysts_foreign': autocatalysts_foreign, 'methods':methods, 'cities': cities}
    response.write(t.render(c))
    return response