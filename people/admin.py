from django.contrib import admin
from people.models import People


class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "role_type")
    search_fields = ("name", "role", "role_type")
    
admin.site.register(People, PersonAdmin)