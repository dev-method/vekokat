from django.contrib import admin
from catalog.models import AutoCatalog, CatalogAdmin, CatalyzatorCategory, CatalyzatorCategoryAdmin, CatalCatFoto, CatalCatFotoAdmin

# Register your models here.
admin.site.register(AutoCatalog, CatalogAdmin)
admin.site.register(CatalyzatorCategory, CatalyzatorCategoryAdmin)
admin.site.register(CatalCatFoto, CatalCatFotoAdmin)

