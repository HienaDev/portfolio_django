from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    ano = models.PositiveIntegerField()
    semestre = models.PositiveSmallIntegerField(choices=[(1, '1º Semestre'), (2, '2º Semestre')])
    docentes = models.ManyToManyField('Docente', related_name='disciplinas')
    link_moodle = models.URLField(blank=True)
    link_site_ulusofona = models.URLField(blank=True)
    conceitos_aplicados = models.TextField(help_text="Conceitos abordados na disciplina.")

    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    foto = models.ImageField(upload_to='docentes/fotos/', null=True, blank=True)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    numero_aluno = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    foto = models.ImageField(upload_to='alunos/fotos/', null=True, blank=True)

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    site_link = models.URLField(blank=True)
    logo = models.ImageField(upload_to='tecnologias/logos/')
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateField()
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)
    alunos = models.ManyToManyField('Aluno', blank=True)
    tecnologias = models.ManyToManyField('Tecnologia', blank=True)
    desafios = models.TextField()
    github_link = models.URLField(blank=True)
    video_demo_link = models.URLField(blank=True)
    link_projeto = models.URLField(blank=True, verbose_name="Link to Project on Itch.io")

    def __str__(self):
        return self.titulo


class Imagem(models.Model):
    imagem = models.ImageField(upload_to='projetos/imagens/')
    legenda = models.CharField(max_length=255, blank=True)

    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='imagens')

    def __str__(self):
        return f"Imagem do projeto: {self.projeto.titulo}"
