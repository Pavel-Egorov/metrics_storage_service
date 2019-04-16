import os

from django.contrib.admin.sites import AdminSite

APP_NAME = os.environ['APP_NAME']


class ServiceAdminSite(AdminSite):
    site_header = "Admin Interface"
    site_title = APP_NAME
    index_title = APP_NAME


admin_site = ServiceAdminSite()
