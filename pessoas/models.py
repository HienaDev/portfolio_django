from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, default='nome')
    idade = models.IntegerField(default = -1)
    profissao = models.CharField(max_length=100, default = 'profissão')
    salario = models.IntegerField(default = -1)

    def __str__(self):
        return f'{self.nome}: {self.idade} anos\n{self.profissao}: {self.salario} euros'