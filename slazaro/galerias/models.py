# -*- encoding: utf-8 -*-

from django.db import models

class Galeria(models.Model):

	nombre      = models.CharField(max_length = 255)
	descripcion = models.TextField(u'descripción', blank = True)
	creado      = models.DateTimeField(u'fecha de creación', auto_now_add = True)
	modificado  = models.DateTimeField(u'última modificación', auto_now = True)


	def __unicode__(self):

		return self.nombre


class Imagen(models.Model):

	galeria     = models.ForeignKey(Galeria)
	imagen      = models.ImageField(upload_to = 'imagenes')
	descripcion = models.TextField(u'descripción', blank = True)
	creado      = models.DateTimeField(u'fecha de creación', auto_now_add = True)


	def thumb(self):

		if self.imagen:

			return '<img src="/media/%s" width="100">' % self.imagen

		return 'Agregar Imagen'


	thumb.allow_tags        = True
	thumb.short_description = 'thumb'


	def __unicode__(self):

		return self.imagen


	class Meta:

		verbose_name_plural = u'imagenes'