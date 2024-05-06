from django.contrib import admin
from people.models import People, JobRole, BoardPosition, TeamList


class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "team", "board_position")
    search_fields = ("name", "role", "team", "board_position")


class JobRoleAdmin(admin.ModelAdmin):
    list_display = ("role",)
    search_fields = ("role",)

class BoardPositionAdmin(admin.ModelAdmin):
    list_display = ("role",)
    search_fields = ("role",)

class TeamListAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(People, PersonAdmin)
admin.site.register(JobRole, JobRoleAdmin)
admin.site.register(BoardPosition, BoardPositionAdmin)
admin.site.register(TeamList, TeamListAdmin)

