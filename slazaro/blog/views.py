# -*- encoding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post

def index(request):

	posts = Post.objects.all().filter(estado = 'p', destacado = True, categoria__nombre__iexact = 'noticias')[:4]
	context = {
		'posts' : posts,
	}

	return render(request, 'blog/index.html', context)