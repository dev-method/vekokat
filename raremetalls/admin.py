# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from raremetalls.models import PlatinumPrice, TantalPrice, RhodyiPrice

# Register your models here.
admin.site.register(PlatinumPrice)
admin.site.register(TantalPrice)
admin.site.register(RhodyiPrice)
