from django.conf import settings
from django.contrib.admin.sites import AdminSite

from api_impl import admin, models


class ServiceAdminSite(AdminSite):
    site_header = "Admin Interface"
    site_title = settings.APP_NAME
    index_title = settings.APP_NAME


admin_site = ServiceAdminSite()

admin_site.register(models.AdvertisementMetric, admin.AdvertisementMetricAdmin)
