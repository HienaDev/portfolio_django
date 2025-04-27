from django.contrib import admin

from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade","profissao","salario",)
    ordering = ("nome", "idade","profissao","salario",)
    search_fields = ("nome",)

admin.site.register(Pessoa, PessoaAdmin)



