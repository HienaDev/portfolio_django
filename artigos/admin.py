from django.contrib import admin
from .models import Autor, Artigo, Comment, Rating

# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nome", "data_criacao","foto")
    ordering =  ("nome", "data_criacao")
    search_fields = ("nome","data_criacao")

admin.site.register(Autor, AutorAdmin)

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "data_criacao", "author", "link")
    ordering =  ("titulo", "data_criacao", "author")
    search_fields = ("titulo", "author")

admin.site.register(Artigo, ArtigoAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("artigo", "autor", "data_criacao", "comentario")
    ordering =  ("artigo", "autor","data_criacao", "comentario")
    search_fields = ("artigo", "autor", "data_criacao","comentario")


admin.site.register(Comment, CommentAdmin)

class RatingAdmin(admin.ModelAdmin):
    list_display = ("classificacao", "data_criacao")
    ordering =  ("classificacao","data_criacao")
    search_fields = ("classificacao", "data_criacao")


admin.site.register(Rating, RatingAdmin)