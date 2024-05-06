from django.shortcuts import render

from people.models import People

def people(request):
    people = People.objects.filter(team__name="Diretoria").all()
    # aula #F38 - filtros com parâmetros
    # criar classe cargos e ordenar por cargos

    return render(request, "diretoria.html", context={"people": people})
