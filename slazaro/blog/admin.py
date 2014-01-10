from django.contrib import admin
from blog.models import Categoria, Tag, Post, Comentario


admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comentario)