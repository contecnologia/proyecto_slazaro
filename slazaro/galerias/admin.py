from django.contrib import admin
from galerias.models import Galeria, Imagen

class ImagenesInline(admin.TabularInline):

	model           = Imagen
	extra           = 1
	fields          = ('thumb', 'imagen', 'descripcion',)
	readonly_fields = ('thumb',)


class GaleriaAdmin(admin.ModelAdmin):

	inlines = [ImagenesInline]


admin.site.register(Galeria, GaleriaAdmin)