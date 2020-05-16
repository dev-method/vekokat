from django.contrib import admin
from cities.models import City, CityAdmin

# Register your models here.
admin.site.register(City, CityAdmin)