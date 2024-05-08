from django.contrib import admin

from company_entity.models import Company, SiteFooter


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "company_name",
        "trade_name",
        "cnpj",
        "state_registration",
        "municipal_registration",
        "address",
        "phone",
        "email",
        "website",
        "opening_date",
        "main_activity",
        "secondary_activity",
        "responsible_name",
        "notes",
    )
    search_fields = ("company_name", "trade_name", "cnpj")

class SiteFooterAdmin(admin.ModelAdmin):
    list_display = ("name", "service_hours", "main_footer")
    search_fields = ("id", "name")

admin.site.register(Company, CompanyAdmin)
admin.site.register(SiteFooter, SiteFooterAdmin)
