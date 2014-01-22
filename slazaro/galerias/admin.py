from django.contrib import admin
from galerias.models import Galeria, Imagen

class ImagenesInline(admin.TabularInline):

	model           = Imagen
	extra           = 1
	fields          = ('thumb', 'imagen', 'descripcion',)
	readonly_fields = ('thumb',)


class GaleriaAdmin(admin.ModelAdmin):

	fields          = ('nombre', 'descripcion', 'post',)
	inlines         = [ImagenesInline]
	raw_id_fields   = ('post',)


admin.site.register(Galeria, GaleriaAdmin)