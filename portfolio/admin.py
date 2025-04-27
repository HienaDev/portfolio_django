from django.contrib import admin
from .models import Projeto, Disciplina, Aluno, Docente, Tecnologia, Imagem


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "descricao", "github_link", "video_demo_link", "disciplina")
    ordering = ("titulo", "disciplina")
    search_fields = ("titulo", "descricao", "github_link", "video_demo_link")

admin.site.register(Projeto, ProjetoAdmin)


class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano", "semestre", "link_moodle", "link_site_ulusofona")
    ordering = ("nome", "ano", "semestre")
    search_fields = ("nome", "ano", "semestre", "docentes__nome")

admin.site.register(Disciplina, DisciplinaAdmin)


class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "numero_aluno", "email")
    ordering = ("nome", "numero_aluno")
    search_fields = ("nome", "numero_aluno", "email")

admin.site.register(Aluno, AlunoAdmin)


class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    ordering = ("nome",)
    search_fields = ("nome", "email")

admin.site.register(Docente, DocenteAdmin)


class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao", "site_link")
    ordering = ("nome",)
    search_fields = ("nome", "descricao", "site_link")

admin.site.register(Tecnologia, TecnologiaAdmin)


class ImagemAdmin(admin.ModelAdmin):
    list_display = ("projeto", "imagem", "legenda")
    ordering = ("projeto",)
    search_fields = ("projeto__titulo", "legenda")

admin.site.register(Imagem, ImagemAdmin)
