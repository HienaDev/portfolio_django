from django.contrib import admin
from .models import Band, Album, Music
# Register your models here.

class BandAdmin(admin.ModelAdmin):
    list_display = ("nome", "nr_elementos","ano_criacao", "foto")
    ordering =  ("nome", "nr_elementos","ano_criacao")
    search_fields = ("nome", "nr_elementos","ano_criacao")

admin.site.register(Band, BandAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ("nome", "nr_musicas", "band", "spotify_link","capa")
    ordering =  ("nome", "nr_musicas", "band")
    search_fields = ("nome", "banda")

admin.site.register(Album, AlbumAdmin)

class MusicAdmin(admin.ModelAdmin):
    list_display = ("nome", "duration", "album", "lyrics", "spotify_link")
    ordering =  ("nome", "duration", "album")
    search_fields = ("nome", "album", "lyrics")


admin.site.register(Music, MusicAdmin)

