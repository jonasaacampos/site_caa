from django.shortcuts import render

def iframe_documents_view(request):
    # retorna o portal da transparâncida da prefeitura
    return render(request, "documents.html")