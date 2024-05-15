from django.urls import path
from home_page.views import BannerView, index


urlpatterns = [
    path("",  index, name="index"),
    path("", BannerView.as_view(), name="header_banner"),
    ]
