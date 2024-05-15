from django.db import models


class HeaderBanner(models.Model):
    image = models.ImageField(
        upload_to="header_banners/",
        null=False,
        blank=False,
        verbose_name="Header Banner Image",
    )
    title = models.CharField(
        max_length=40, verbose_name="Título", null=False, blank=False
    )
    description = models.CharField(max_length=140, verbose_name="Descrição")
    call_to_action_button_text = models.CharField(
        max_length=40,
        verbose_name="Texto do botão de chamada à ação",
        null=False,
        blank=False,
    )
    button_link = models.URLField(verbose_name="link", null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Banner do cabeçalho"
        verbose_name_plural = "Banners do cabeçalho"

    @property
    def image_url(self):
        if self.image and hasattr(self.image, "url"):
            return self.image.url
        else:
            return ""
