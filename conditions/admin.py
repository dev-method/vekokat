from django.contrib import admin
from conditions.models import ConditionsSeo, Conditions, ConditionsAdmin

# Register your models here.
admin.site.register(ConditionsSeo)
admin.site.register(Conditions, ConditionsAdmin)

