from django.conf.urls import url

from .views import TempView

urlpatterns = [
    url(r'^$', TempView.as_view(), name='temp'),
]
