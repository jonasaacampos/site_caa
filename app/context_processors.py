from company_entity.models import Company, SiteFooter


def context_company(request):
    company = Company.objects.all().first()
    return {'company': company}


def context_footer(request):
    footer = SiteFooter.objects.filter(main_footer=True).first()
    return {'footer': footer}