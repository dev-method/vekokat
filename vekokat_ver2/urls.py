from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.conf import settings
from core import views as coreviews
from contacts import views as contactviews
from catalog import views as catalog_views
from conditions import views as conditions_views
from raremetalls import views as rare_views
from forms import views as forms_vews
from vekokat_ver2.sitemaps import StaticViewSitemap, CatCategorySitemap, AutoCatalogSitemap, CitySitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from contacts.decorators import check_recaptcha
from core.decorators import check_core_recaptcha
from cities import views as cities_views

sitemaps={
    'static':StaticViewSitemap,
    'categories': CatCategorySitemap,
    'models': AutoCatalogSitemap,
    'cities': CitySitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', check_core_recaptcha(coreviews.mainpage_newdesign), name="main-newdesign"),
    path('sw.js', TemplateView.as_view(template_name="core/serviceWorker/sw.js", content_type="text/javascript"), name="sw"),
    path('contacts/', check_recaptcha(contactviews.new_contacts), name="new-contacts"),
    path('catalog/otechestvennyj/', catalog_views.otechcatalog_view, name="otechcatalog-view"),
    path('catalog/otechestvennyj/<slug:slug>/', catalog_views.otechcatalog_item_view, name="otechcatalog-item-view"),
    path('catalog/importnye/', catalog_views.importcatalog_view, name="importcatalog-view"),
    path('catalog/importnye/<slug:slug>/', catalog_views.importcatalog_item_view, name="importcatalog-item-view"),
    path('conditions/', conditions_views.conditions, name="conditions"),
    path('map-interactive/', coreviews.map_intaractive, name="map_intaractive"),
    path('catalizators/<slug:slug>/', catalog_views.catalizator_type_view, name="catalizator-type-view"),
    path('priem-katalizatorov/<slug:slug>/', cities_views.city_view, name="city_view"),

    #FORM-HANDLERS

    path('amp/form-handler/', forms_vews.form_amp_handler, name="form_amp_handler"),
    path('rss/form-handler/', forms_vews.form_rss_handler, name="form_rss_handler"),
    path('form-handler/', check_recaptcha(coreviews.form_handler), name="form_handler"),

    #AMP-PAGES

    path('amp/', coreviews.new_core_amp, name="new-core-amp"),
    path('amp/conditions/', conditions_views.conditions_amp, name="conditions-amp"),
    path('amp/catalog/otechestvennyj/', catalog_views.otechcatalog_amp, name="otechcatalog-amp"),
    path('amp/catalog/otechestvennyj/<slug:slug>/', catalog_views.otechcatalog_item_amp, name="otechcatalog-item-amp"),
    path('amp/catalog/importnye/', catalog_views.importcatalog_amp, name="importcatalog-amp"),
    path('amp/catalog/importnye/<slug:slug>/', catalog_views.importcatalog_item_amp, name="importcatalog-item-amp"),
    path('amp/catalizators/<slug:slug>/', catalog_views.catalizator_type_amp, name="catalizator-type-amp"),
    path('amp/priem-katalizatorov/<slug:slug>/', cities_views.amp_city_view, name="amp_city_view"),

    #TURBO-PAGES

    path('turbo/',coreviews.new_core_rss, name="new-core-rss"),
    path('turbo/catalog/otechestvennyj/',catalog_views.otechcatalog_rss, name="otechcatalog_rss"),
    path('turbo/catalog/importnye/',catalog_views.importcatalog_rss, name="importcatalog_rss"),
    path('turbo/catalog/otechestvennyj/item/',catalog_views.otechcatalog_item_rss, name="otechcatalog_item_rss"),
    path('turbo/catalog/importnye/item/',catalog_views.importcatalog_item_rss, name="importcatalog_item_rss"),
    path('turbo/catalizators/otechestvennye-katalizatory/',catalog_views.catal_otech_rss, name="catal_otech_rss"),
    path('turbo/catalizators/importnye-katalizatory/',catalog_views.catal_imort_rss, name="catal_imort_rss"),
    path('turbo/catalizators/otechestvennye-metallicheskie-katalizatory/',catalog_views.catal_metal_otech_rss, name="catal_metal_otech_rss"),
    path('turbo/catalizators/importnye-metallicheskie-katalizatory/',catalog_views.catal_metal_import_rss, name="catal_metal_import_rss"),
    path('turbo/catalizators/sazhevye-filtry/',catalog_views.sazhev_rss, name="sazhev_rss"),
    path('turbo/conditions/', conditions_views.conditions_rss, name="conditions_rss"),
    path('turbo/priem-katalizatorov/', cities_views.cities_rss, name="cities_rss"),

    #API-ROUTES

    path('api/platinum/', rare_views.platinum_api, name="platinum_api"),
    path('api/palladium/', rare_views.palladium_api, name="palladium_api"),
    path('api/catalog/', catalog_views.catalog_api, name="catalogs_api"),
    path('api/foreign-catalog/', catalog_views.foreign_catalog_api, name="foreign_catalogs_api"),
    path('api/rhodyi/', rare_views.rhodyi_api, name="rhodyi_api"),
    path('api/advantages/',coreviews.advantages_api, name="advantages-api"),
    path('api/working-methods/',coreviews.working_methods_api, name="working-methods-api"),
    path('api/laboratory-api/',coreviews.laboratory_api, name="laboratory-api"),
    path('api/regions-api/',coreviews.regions_api, name="regions-api"),
    path('api/price-blocks-api/',coreviews.price_blocks_api, name="price-blocks-api")
]

handler503 = coreviews.maintainance
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()