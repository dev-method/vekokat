from django.shortcuts import render
from vekokat_ver2.settings import DEBUG
from django.http import HttpResponse
from django.template import loader
from conditions.models import Conditions, ConditionsSeo
from core.models import NewWorkingMethods

# Create your views here.
def conditions(request):
    seo = ConditionsSeo.objects.all()
    methods = NewWorkingMethods.objects.all().order_by("group")
    conditions = Conditions.objects.all()
    if DEBUG:
        return render(request, 'conditions/dev/conditions.html', {'seo': seo, 'conditions':conditions, 'methods':methods})
    else:
        return render(request, 'conditions/prod/conditions.html', {'seo': seo, 'conditions':conditions, 'methods':methods})

def conditions_amp(request):
    seo = ConditionsSeo.objects.all()
    methods = NewWorkingMethods.objects.all().order_by("group")
    conditions = Conditions.objects.all()
    return render(request, 'conditions/amp/conditions-amp.html', {'seo': seo, 'conditions':conditions, 'methods':methods})


def conditions_rss(request):
    seo = ConditionsSeo.objects.all()
    methods = NewWorkingMethods.objects.all().order_by("group")
    conditions = Conditions.objects.all()
    response = HttpResponse(content_type='text/rss')
    response['Content-Disposition'] = 'attachment;filename = "conditions.rss"'
    t = loader.get_template('conditions/yandex-turbo/conditions.rss')
    c = {'seo': seo, 'conditions':conditions, 'methods':methods}
    response.write(t.render(c))
    return response
