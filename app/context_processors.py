from company_entity.models import Company, SiteFooter
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

#############
# home_page #
#############

def context_header_banner(request):
    header_banner = HeaderBanner.objects.all()
    return {'header_banner': header_banner}