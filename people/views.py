from django.shortcuts import render

from people.models import People

def people(request):
    people = People.objects.all()

    return render(request, "people.html", context={"people": people})
