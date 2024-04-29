from django.db import models


class People(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    role = models.ForeignKey("JobRole", on_delete=models.PROTECT,related_name="people_jobRole", null=True, blank=True)
    photo = models.ImageField(upload_to="people/photos/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    role_type = models.CharField(
        max_length=100,
        choices=[
            ("Diretoria", "Diretoria"),
            ("Equipe", "Equipe"),
            ("Voluntário", "Voluntário"),
            ("Estágiário", "Estágiário"),
        ],
        default="Voluntário",
        blank=False, null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.id}'
    
class JobRole(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.role