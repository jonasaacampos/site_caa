from django.db import models


class Company(models.Model):
    
    # Dados Gerais
    id = models.AutoField(primary_key=True)
    logo = models.ImageField(
        upload_to="company_entity/logos", verbose_name="Logo", null=True, blank=True
    )
    company_name = models.CharField(max_length=100, verbose_name="Nome da Empresa")
    trade_name = models.CharField(max_length=100, verbose_name="Nome Fantasia")
    
    # Registros da empresa
    cnpj = models.CharField(max_length=14, verbose_name="CNPJ")
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
    social_media_facebook = models.URLField(blank=True, null=True, verbose_name="Facebook") 
    social_media_instagram = models.URLField(blank=True, null=True, verbose_name="Instagram") 
    social_media_whatsapp = models.URLField(blank=True, null=True, verbose_name="WhatsApp") 
    social_media_linkedin = models.URLField(blank=True, null=True, verbose_name="Linkedin") 

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
    notes = models.TextField(verbose_name="Observações", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em",
    )

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ["id"]


class SiteFooter(models.Model):
    id = models.AutoField(primary_key=True)
    main_footer = models.BooleanField(
        editable=True, default=True, verbose_name="Rodapé Principal"
    )
    name = models.CharField(
        max_length=100,
        default="Rodapé padrão do site",
        verbose_name="Nome do rodapé (controle interno)",
    )
    service_hours = models.CharField(
        max_length=100, verbose_name="Horário de Atendimento"
    )
    line_text1 = models.CharField(max_length=200, verbose_name="Texto da Linha 1")
    line_text2 = models.CharField(max_length=200, verbose_name="Texto da Linha 2")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Rodapé do Site"
        verbose_name_plural = "Rodapés do Site"
        ordering = ["id"]
