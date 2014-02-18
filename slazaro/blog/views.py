# -*- encoding: utf-8 -*-

from django.core.mail import send_mail, BadHeaderError 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Categoria, Tag

def index(request):

	posts = Post.objects.all().filter(estado = 'p', destacado = True, categoria__nombre__iexact = 'noticias')[:4]
	context = {
		'posts' : posts,
	}

	return render(request, 'blog/index.html', context)


def miembros(request):

	post = Post.objects.get(tags__nombre__iexact = 'miembros')
	context = {
		'post' : post,
	}

	return render(request, 'blog/secciones.html', context)


def testimonios(request):

	post = Post.objects.get(tags__nombre__iexact = 'testimonios')
	context = {
		'post' : post,
	}

	return render(request, 'blog/secciones.html', context)


def donaciones(request):

	post = Post.objects.get(tags__nombre__iexact = 'donaciones')
	context = {
		'post' : post,
	}

	return render(request, 'blog/secciones.html', context)


def contacto(request):

	if request.method == 'POST':

		nombre     = request.POST.get('nombre')
		email      = request.POST.get('email')
		telefono   = request.POST.get('telefono')
		asunto     = request.POST.get('asunto')
		mensaje_d  = request.POST.get('mensaje')
		mensaje    = """
		Nombre   : %s
		E-Mail   : %s
		Telefono : %s
		Asunto   : %s
		Mensaje  :
		%s
		""" % (nombre, email, telefono, asunto, mensaje_d)

		if nombre and email and asunto and mensaje_d:

			try:

				send_mail(asunto, mensaje, email, ['ernesto@contecnologia.com'], fail_silently = False)

			except BadHeaderError:

				return HttpResponse("Error en las cabeceras del email.")


			return HttpResponseRedirect('/contacto/gracias/')

		else:

			return HttpResponse("Faltan Datos")

	else:

		return render(request, 'blog/contacto.html')


# Vistas del blog

def blog_index(request):

	posts_list = Post.objects.filter(estado = 'p').exclude(categoria__nombre__iexact = 'paginas').order_by('-modificado')
	paginator = Paginator(posts_list, 5)
	page = request.GET.get('page')

	try:

		posts = paginator.page(page)

	except PageNotAnInteger:

		posts = paginator.page(1)

	except EmptyPage:

		posts = paginator.page(paginator.num_pages)


	context = {
		'posts'      : posts,
		'categorias' : __get_categorias(),
		'tags'       : __get_tags(),
	}

	return render(request, 'blog/blog_posts.html', context)


def blog_post(request, post_id):

	post = get_object_or_404(Post, pk = post_id)
	context = {
		'post'       : post,
		'categorias' : __get_categorias(),
		'tags'       : __get_tags()
	}

	return render(request, 'blog/blog_post.html', context)


def blog_cat(request, cat_id):

	posts_list = Post.objects.filter(categoria__id = cat_id).order_by('-modificado')
	paginator = Paginator(posts_list, 5)
	page = request.GET.get('page')

	try:

		posts = paginator.page(page)

	except PageNotAnInteger:

		posts = paginator.page(1)

	except EmptyPage:

		posts = paginator.page(paginator.num_pages)



	context = {
		'posts'      : posts,
		'categorias' : __get_categorias(),
		'tags'       : __get_tags(),
	}

	return render(request, 'blog/blog_posts.html', context)


def blog_tag(request, tag_id):

	posts_list = Post.objects.filter(tags__id = tag_id).order_by('-modificado')
	paginator = Paginator(posts_list, 5)
	page = request.GET.get('page')

	try:

		posts = paginator.page(page)

	except PageNotAnInteger:

		posts = paginator.page(1)

	except EmptyPage:

		posts = paginator.page(paginator.num_pages)


	context = {
		'posts'      : posts,
		'categorias' : __get_categorias(),
		'tags'       : __get_tags()
	}

	return render(request, 'blog/blog_posts.html', context)


def busqueda(request):

	return HttpResponse('busqueda')


def __get_categorias():

	return Categoria.objects.all().exclude(nombre__iexact = 'Paginas')

def __get_tags():

	return Tag.objects.all().exclude(nombre__iexact = 'testimonios').exclude(nombre__iexact = 'miembros').exclude(nombre__iexact = 'donaciones')