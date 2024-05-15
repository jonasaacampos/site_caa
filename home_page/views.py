from django.shortcuts import render
from django.views.generic import ListView
from .models import HeaderBanner

def index(request):
    return render(request, 'index.html')


class BannerView(ListView):
    model = HeaderBanner
    template_name = 'index.html'
    context_object_name = 'header_banner'
    
    def get_queryset(self):
        return super().get_queryset().all()
    
