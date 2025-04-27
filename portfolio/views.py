# Create your views here.
# portfolio/views.py

from django.shortcuts import render, get_object_or_404
from .models import Projeto, Aluno, Docente, Disciplina, Tecnologia
from datetime import datetime

current_day = datetime.now().day
current_month = datetime.now().month
current_year = datetime.now().year

def index_view(request):
    # busca todos os projetos
    projetos = Projeto.objects.all()
    # data atual
    hoje = datetime.now()
    context = {
        'projetos': projetos,
    }
    return render(request, 'portfolio/index.html', context)

def sobre_view(request):
    return render(request, "portfolio/sobre.html")

def interesses_view(request):
    return render(request, "portfolio/interesses.html")

def projeto_detalhe(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'portfolio/projeto_detalhe.html', {'projeto': projeto})

def aluno_detalhe(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    projetos = aluno.projeto_set.all()  # projetos em que este aluno participa
    disciplinas = set(projeto.disciplina for projeto in projetos)  # disciplinas únicas
    return render(request, 'portfolio/aluno_detalhe.html', {
        'aluno': aluno,
        'projetos': projetos,
        'disciplinas': disciplinas,
    })

def docente_detalhe(request, docente_id):
    docente = get_object_or_404(Docente, id=docente_id)


    disciplinas = docente.disciplinas.all()

    projetos = Projeto.objects.filter(disciplina__in=disciplinas)

    return render(request, 'portfolio/docente_detalhe.html', {
        'docente': docente,
        'projetos': projetos,
        'disciplinas': disciplinas,
    })

def disciplina_detalhe(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    return render(request, 'portfolio/disciplina_detalhe.html', {
        'disciplina': disciplina,
    })

def tecnologia_detalhe(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, pk=tecnologia_id)
    projetos = Projeto.objects.filter(tecnologias=tecnologia)

    context = {
        'tecnologia': tecnologia,
        'projetos': projetos,

    }

    return render(request, 'portfolio/tecnologia_detalhe.html', context)

def tecnologias(request):
    tecnologias = Tecnologia.objects.all()

    context = {
        'tecnologias': tecnologias,

    }

    return render(request, 'portfolio/tecnologias.html', context)

def cv_view(request):
    return render(request, 'portfolio/cv.html')


