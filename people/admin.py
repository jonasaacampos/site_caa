from django.contrib import admin
from people.models import People, JobRole


class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "role_type")
    search_fields = ("name", "role", "role_type")


class JobRoleAdmin(admin.ModelAdmin):
    list_display = ("role",)
    search_fields = ("role",)


admin.site.register(People, PersonAdmin)
admin.site.register(JobRole, JobRoleAdmin)
