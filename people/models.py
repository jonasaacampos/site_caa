from django.db import models


class People(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False, verbose_name="Nome")
    role = models.ForeignKey(
        "JobRole",
        on_delete=models.PROTECT,
        related_name="people_jobRole",
        null=True,
        blank=True,
        verbose_name="Cargo",
    )
    photo = models.ImageField(upload_to="people/", blank=True, null=True, verbose_name="Foto")
    bio = models.TextField(blank=True, null=True)

    team = models.ForeignKey(
        "TeamList",
        on_delete=models.PROTECT,
        related_name="people_team",
        null=False,
        blank=False,
        default=1,
        verbose_name="Equipe",
    )

    board_position = models.ForeignKey(
        "BoardPosition",
        on_delete=models.PROTECT,
        related_name="board_position",
        null=True,
        blank=True,
        verbose_name="Posição na Diretoria",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def if_photo_is_blank(self):
        # insere uma photo padrão caso o campo esteja vazio
        if not self.photo or self.photo.strip() == "":
            self.photo = "people/default_no_photo_avatar.png"
        return False

    def save(self, *args, **kwargs):
        self.if_photo_is_blank()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class JobRole(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.role


class BoardPosition(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.role


class TeamList(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
