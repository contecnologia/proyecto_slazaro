# -*- encoding: utf-8 -*-

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
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

	return render(request, 'blog/miembros.html', context)


def testimonios(request):

	post = Post.objects.get(tags__nombre__iexact = 'testimonios')
	context = {
		'post' : post,
	}

	return render(request, 'blog/miembros.html', context)


def donaciones(request):

	post = Post.objects.get(tags__nombre__iexact = 'donaciones')
	context = {
		'post' : post,
	}

	return render(request, 'blog/donaciones.html', context)


def contacto(request):

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

	posts_list = Post.objects.filter(categoria__id = cat_id)
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

	posts_list = Post.objects.filter(tags__id = tag_id)
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