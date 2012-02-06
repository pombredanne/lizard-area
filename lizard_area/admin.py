from django.contrib.gis import admin

from lizard_area.models import GeoObject
from lizard_area.models import GeoObjectGroup

from lizard_area.models import Category
from lizard_area.models import MapnikXMLStyleSheet

from lizard_area.models import AreaWFSConfiguration
from lizard_area.models import SynchronizationHistory
from lizard_area.models import DataAdministrator
from lizard_area.models import Communique
from lizard_area.models import Area


class GeoObjectInline(admin.TabularInline):
    model = GeoObject


class GeoObjectGroupAdmin(admin.ModelAdmin):
    inlines = [
        GeoObjectInline,
        ]


class AreaAdmin(admin.ModelAdmin):
    list_filter = ('data_set', 'area_class', )
    list_display = ('name', 'ident', 'id', 'area_class')


# admin.site.register(GeoObject)
admin.site.register(GeoObjectGroup, GeoObjectGroupAdmin)

admin.site.register(Category)
admin.site.register(MapnikXMLStyleSheet)

admin.site.register(DataAdministrator)
admin.site.register(Communique)
admin.site.register(Area, AreaAdmin)
admin.site.register(AreaWFSConfiguration)
admin.site.register(SynchronizationHistory)
