from django.conf.urls import include, url

from .admin import admin_site

urlpatterns = [
    url(r'^admin/', admin_site.urls),
    url(r'', include('api_impl.urls')),
]
