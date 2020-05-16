from celery import shared_task
from django.core.mail import send_mail

@shared_task(acks_late=True)
def send_order(name, phone_mail, model, year, valcat, typecat):
    subject="Имя:  "+name+"\n"+"Телефон или почта:  "+phone_mail+"\n"+"Марка|модель автомобиля:  "+model+"\n"+"Год выпуска:  "+year+"\n"+"Объем|тип мотора (дизель|бензин):  "+valcat+"\n"+"Тип катализатора (керамика|металл):  "+typecat
    send_mail('Запрос на обратную связь', subject, 'admin@vekomet.ru', ['vekokat@gmail.com'], fail_silently=False)
    print("success")