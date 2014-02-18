# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^miembros/$', views.miembros, name = 'miembros'),
	url(r'^testimonios/$', views.testimonios, name = 'testimonios'),
	url(r'^donaciones/$', views.donaciones, name = 'donaciones'),
	url(r'^contacto/$', views.contacto, name = 'contacto'),
	url(r'^contacto/gracias/$', TemplateView.as_view(template_name = 'gracias.html')),

	# URLs del Blog
	url(r'^blog/$', views.blog_index, name = "blog"),                             # Vista del Blog
	url(r'^(?P<post_id>\d+)/blog/$', views.blog_post, name = 'blog_post'),        # Vista de Post
	url(r'^(?P<cat_id>\d+)/categoria/blog/$', views.blog_cat, name = 'blog_cat'), # Vista de Posts por Categoría
	url(r'^(?P<tag_id>\d+)/tag/blog/$', views.blog_tag, name = 'blog_tag'),	      # Vista de Posts por Tag
)