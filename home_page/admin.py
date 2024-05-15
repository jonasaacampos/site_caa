from django.contrib import admin
from home_page.models import HeaderBanner

class HeaderBannerAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "call_to_action_button_text", "button_link")
    search_fields = ("title", "description")


admin.site.register(HeaderBanner)
