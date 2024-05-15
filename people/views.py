from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView

from people.models import People

def people(request):
    people = People.objects.filter(team__name="Diretoria").all()
    # aula #F38 - filtros com parâmetros
    # criar classe cargos e ordenar por cargos
    # ver aula 56 - List view

    return render(request, "diretoria.html", context={"people": people})

class Diretoria(ListView):
    model = People
    template_name = 'diretoria.html'
    context_object_name = 'diretoria'

    def get_queryset(self) -> QuerySet[Any]:
        only_board_members = super().get_queryset().filter(team__name="Diretoria").all()
        return only_board_members


