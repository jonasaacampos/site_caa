from django.db import models


class People(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    role = models.ForeignKey(
        "JobRole",
        on_delete=models.PROTECT,
        related_name="people_jobRole",
        null=True,
        blank=True,
    )
    photo = models.ImageField(upload_to="people/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    team = models.ForeignKey(
        "TeamList",
        on_delete=models.PROTECT,
        related_name="people_team",
        null=True,
        blank=True,
    )

    board_position = models.ForeignKey(
        "BoardPosition",
        on_delete=models.PROTECT,
        related_name="board_position",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.id}"
    
    class Meta: 
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    # def save(self, *args, **kwargs):
    #     if self.role:
    #         self.role = self.role.upper()
    #     super(People, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.if_photo_is_blank()
        super().save(*args, **kwargs)
        
    def if_photo_is_blank(self):
        # insere uma photo padrão caso o campo esteja vazio
        if self.photo == "":
            self.photo = "people/default_no_photo_avatar.png"
            
        return False
    


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


