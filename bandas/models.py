from django.db import models

# Create your models here.
# Create your models here.
class Band(models.Model):
    nome = models.CharField(max_length=100, default='nome')
    nr_elementos = models.IntegerField(default = -1)
    ano_criacao = models.IntegerField(default = 1900)
    foto = models.ImageField(null = True, blank = True)

    def __str__(self):
        return f'{self.nome}: {self.nr_elementos} elementos'

class Album(models.Model):
    nome = models.CharField(max_length=100, default='nome')
    nr_musicas = models.IntegerField(default = -1)
    band = models.ForeignKey(Band, default="Sem banda", on_delete=models.SET_DEFAULT)
    spotify_link = models.CharField(max_length=200, default='link')
    capa = models.ImageField(null = True, blank = True)


    def __str__(self):
        return f'{self.band} - {self.nome}: {self.nr_musicas} musicas'

class Music(models.Model):
    nome = models.CharField(max_length=100, default='nome')
    duration = models.IntegerField(default = -1)
    album = models.ForeignKey(Album, default="Sem album", on_delete=models.SET_DEFAULT)
    spotify_link = models.TextField (default='link')
    lyrics = models.TextField (default='letra')

    def __str__(self):
        return f'{self.album} - {self.nome}: {self.duration} segundos'