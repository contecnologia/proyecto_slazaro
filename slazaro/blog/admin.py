# -*- encoding: utf-8 -*-

from django.contrib import admin
from blog.models import Categoria, Tag, Post, Comentario

class PostAdmin(admin.ModelAdmin):

	fieldsets          = [
		(
			None,
			{
				'fields' : (
					'titulo', 'contenido',
				)
			}
		),
		(
			'Categorización',
			{
				'fields' : (
					'categoria', 'tags', 'estado', 'destacado',
				)
			}
		),
		(
			'Extras',
			{
				'fields' : (
					'creado', 'modificado',
				)
			}
		),
	]
	list_display       = ('titulo', 'usuario', 'categoria', 'estado', 'destacado', 'creado', 'modificado')
	list_editable      = ('estado',)
	list_filter        = ('categoria__nombre', 'estado',)
	search_fields      = ('titulo', 'contenido', 'categoria__nombre', 'usuario__first_name', 'usuario__last_name',)
	filter_horizontal  = ('tags',)
	readonly_fields    = ('creado', 'modificado')


	def save_model(self, request, obj, form, change):

		if not change:

			obj.usuario = request.user

		obj.save()


	class Media:

		js = [
			'/static/js/tinymce/tinymce.min.js',
			'/static/js/tinymce/config.js',
		]


admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario)