from company_entity.models import Company, SiteFooter, Partner
from home_page.models import HeaderBanner

####################
# company_entities #
####################

def context_company(request):
    company = Company.objects.all().first()
    return {'company': company}


def context_footer(request):
    footer = SiteFooter.objects.filter(main_footer=True).first()
    return {'footer': footer}

def context_partner(request):
    partner = Partner.objects.all()
    print(partner)
    return {'partner': partner}

#############
# home_page #
#############

def context_header_banner(request):
    header_banner = HeaderBanner.objects.all()
    return {'header_banner': header_banner}

