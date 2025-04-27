from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Autor(models.Model):
    nome = models.CharField(max_length=100, default='nome')
    foto = models.ImageField(null = True, blank = True)
    data_criacao = models.DateField()

    def __str__(self):
        return f'{self.nome} juntou-se a {self.data_criacao}'

# Create your models here.
class Artigo(models.Model):
    titulo = models.CharField(max_length=100, default='titulo')
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)
    data_criacao = models.DateField()
    link = models.TextField (default='link')

    def __str__(self):
        return f'{self.titulo} criado por {self.author}'

class Comment(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    comentario = models.TextField (default='comentário')
    data_criacao = models.DateField()

    def __str__(self):
        return f'{self.autor} criou comentário: {self.comentario}\nData de criação: {self.data_criacao} segundos'

class Rating(models.Model):

    classificacao = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    article = models.ManyToManyField(Artigo, related_name='ratings')
    data_criacao = models.DateField()


    def __str__(self):
        return f'{self.article} - {self.classificacao}'






