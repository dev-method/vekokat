from django.http import JsonResponse
from orders.models import NewOrder

# Create your views here.
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
                response = JsonResponse({"message":"Сообщение успешно отправлено!"})
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
    success_response = [
        {
            "field": "message",
            "value": "Отправка формы прошла успешно"
        },
        {
            "field": "link",
            "value": "Вернуться на главную",
            "href": "https://vekokat.ru/"
        }]
    error_response = [
        {
            "field": "message",
            "value": "Возникли проблемы с отправкой сообщения. Попробуйте еще раз."
        },
        {
            "field": "link",
            "value": "Вернуться на главную",
            "href": "https://vekokat.ru/"
        }]
    form = {}
    if request.POST:
        form['name'] = request.POST.get('name')
        form['phone_mail'] = request.POST.get('phone_mail')
        form['model'] = request.POST.get('model')
        form['valcat'] = request.POST.get('valcat')
        form['year'] = request.POST.get('year')
        form['typecat'] = request.POST.get('typecat')
        if form['phone_mail']:
                NewOrder.objects.create(name=form['name'], phone_mail=form['phone_mail'], model=form['model'],
                                        year=form['year'], valcat=form['valcat'], typecat=form['typecat'])
                response = JsonResponse(success_response)
                response['AMP-Access-Control-Allow-Source-Origin'] = '*.yandex.*'
                response['AMP-Access-Control-Allow-Source-Origin'] = '*.turbopages.org'
                response['Access-Control-Allow-Credentials'] = 'true'
                response['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Content-Length, Accept-Encoding'
                response['Access-Control-Expose-Headers'] = 'AMP-Access-Control-Allow-Source-Origin'
                response['Content-Type'] = 'application/json;charset=utf-8'
                return response
    response = JsonResponse(error_response)
    response['AMP-Access-Control-Allow-Source-Origin'] = '*.yandex.*'
    response['AMP-Access-Control-Allow-Source-Origin'] = '*.turbopages.org'
    response['Access-Control-Allow-Credentials'] = 'true'
    response['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Content-Length, Accept-Encoding'
    response['Access-Control-Expose-Headers'] = 'AMP-Access-Control-Allow-Source-Origin'
    response['Content-Type'] = 'application/json;charset=utf-8'
    return response
