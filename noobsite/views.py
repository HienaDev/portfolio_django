from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")


def soma(request, a, b):
    return HttpResponse(f"Olá n00b! {a} + {b} = {a + b}!")


def bom_dia(request):
    return HttpResponse("Olá n00b, B0M D14!")


def wow(request):
    return HttpResponse("Wow n00b!")