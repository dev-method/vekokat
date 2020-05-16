# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from core.models import NewSlider, NewSliderAdmin, NewAdvantages, NewWorkingMethods, NewWorkingMethodsAdmin, PartnersBlock, PartnersBlockAdmin
from core.models import NewLaboratory, NewRegions, NewPriceBlock, NewPriceBlockAdmin, NewTextAbout, MainSeo
from core.models import AdvantagesText, MethodsText


# Register your models here.
admin.site.register(NewSlider, NewSliderAdmin)
admin.site.register(NewAdvantages)
admin.site.register(AdvantagesText)
admin.site.register(NewWorkingMethods, NewWorkingMethodsAdmin)
admin.site.register(MethodsText)
admin.site.register(NewLaboratory)
admin.site.register(NewRegions)
admin.site.register(NewPriceBlock, NewPriceBlockAdmin)
admin.site.register(NewTextAbout)
admin.site.register(MainSeo)
admin.site.register(PartnersBlock, PartnersBlockAdmin)
