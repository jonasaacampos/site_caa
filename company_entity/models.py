from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from ckeditor.fields import RichTextField


class Company(models.Model):

    # Dados Gerais
    id = models.AutoField(primary_key=True)
    logo = models.ImageField(
        upload_to="company_entity/logos", verbose_name="Logo", null=True, blank=True
    )
    company_name = models.CharField(max_length=100, verbose_name="Razão Social")
    trade_name = models.CharField(max_length=100, verbose_name="Nome Fantasia")

    is_active = models.BooleanField(
        blank=False, null=False, default=True, verbose_name="Ativo"
    )

    # Registros da empresa
    cnpj = models.CharField(max_length=14, verbose_name="CNPJ", null=True, blank=True)
    state_registration = models.CharField(
        max_length=20, verbose_name="Inscrição Estadual", null=True, blank=True
    )
    municipal_registration = models.CharField(
        max_length=20, verbose_name="Inscrição Municipal", null=True, blank=True
    )

    # Dados de Contato
    address = models.CharField(
        max_length=100, verbose_name="Endereço", null=True, blank=True
    )
    phone = models.CharField(
        max_length=20, verbose_name="Telefone", null=True, blank=True
    )
    email = models.EmailField(
        max_length=100, verbose_name="E-mail", null=True, blank=True
    )
    website = models.URLField(
        max_length=100, verbose_name="Website", null=True, blank=True
    )
    social_media_facebook = models.URLField(
        blank=True, null=True, verbose_name="Facebook"
    )
    social_media_instagram = models.URLField(
        blank=True, null=True, verbose_name="Instagram"
    )
    social_media_whatsapp = models.URLField(
        blank=True, null=True, verbose_name="WhatsApp"
    )
    social_media_linkedin = models.URLField(
        blank=True, null=True, verbose_name="Linkedin"
    )

    # Dados Complementares
    opening_date = models.DateField(
        verbose_name="Data de Abertura", null=True, blank=True
    )
    main_activity = models.CharField(
        max_length=100, verbose_name="Atividade Principal", null=True, blank=True
    )
    secondary_activity = models.CharField(
        max_length=100, verbose_name="Atividade Secundária", null=True, blank=True
    )
    responsible_name = models.CharField(
        max_length=100, verbose_name="Nome do Responsável", null=True, blank=True
    )
    cpf = models.CharField(max_length=14, verbose_name="CPF", null=True, blank=True)

    notes = models.TextField(verbose_name="Observações", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em",
    )

    def __str__(self):
        return self.company_name

    @property
    def logo_url(self):
        if self.logo and hasattr(self.logo, "url"):
            return self.logo.url
        else:
            return ""

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ["id"]


class SiteFooter(models.Model):
    id = models.AutoField(primary_key=True)
    main_footer = models.BooleanField(
        editable=True,
        default=True,
        unique=True,
        verbose_name="Rodapé Principal",
        help_text="Marque para definir como rodapé principal do site",
        error_messages={"unique": "Já existe um rodapé principal definido"},
    )
    name = models.CharField(
        max_length=100,
        default="Rodapé padrão do site",
        verbose_name="Nome do rodapé (controle interno)",
    )
    service_hours = RichTextField(max_length=200, verbose_name="Horário de Atendimento")
    line_text1 = models.CharField(max_length=200, verbose_name="Texto da Linha 1")
    line_text2 = models.CharField(max_length=200, verbose_name="Texto da Linha 2")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Rodapé do Site"
        verbose_name_plural = "Rodapés do Site"
        ordering = ["id"]


class Partner(Company):
    PARTNER_TYPES = {"1": "Parceiro", "2": "Fornecedor"}
    PARTNER_TYPES_PERSON = {"1": "Pessoa Jurídica", "2": "Pessoa Física"}
    role = models.CharField(
        max_length=1,
        choices=PARTNER_TYPES.items(),
        verbose_name="Tipo de Parceiro",
        default="1",
    )

    partner_type = models.CharField(
        max_length=1,
        choices=PARTNER_TYPES_PERSON.items(),
        verbose_name="Natureza do Parceiro",
        default="1",
    )

    class Meta:
        # proxy = True
        verbose_name = "Parceiro"
        verbose_name_plural = "Parceiros"
        ordering = ["id"]
        app_label = "company_entity"
