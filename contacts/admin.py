from django.contrib import admin
from contacts.models import ContactsText, ContactsSeo

# Register your models here.
admin.site.register(ContactsText)
admin.site.register(ContactsSeo)
