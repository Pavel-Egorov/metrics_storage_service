import django_filters

from .models import AdvertisementMetric


class MetricsFilter(django_filters.FilterSet):
    class Meta:
        model = AdvertisementMetric
        fields = {
            'metric_date': ['lt', 'gt'],
            'channel': ['exact'],
            'country': ['exact'],
            'operating_system': ['exact'],
        }
