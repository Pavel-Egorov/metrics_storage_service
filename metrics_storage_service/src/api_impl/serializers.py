from django.conf import settings
from rest_framework import serializers

from .models import AdvertisementMetric
from .utils import DynamicSerializer


class MetricSerializer(DynamicSerializer, serializers.HyperlinkedModelSerializer):
    metric_date = serializers.DateField(
        format=settings.REST_DATE_FORMAT,
        input_formats=[settings.REST_DATE_FORMAT, 'iso-8601'],
    )

    class Meta:
        model = AdvertisementMetric
        fields = [
            'id',
            'metric_date',
            'channel',
            'country',
            'operating_system',
            'impressions_count',
            'clicks_count',
            'installations_count',
            'spend_money',
            'revenue',
            'cpi',
        ]


class GroupedMetricSerializer(DynamicSerializer, serializers.Serializer):
    allowed_groupings = {
        'metric_date',
        'channel',
        'country',
        'operating_system',
    }

    metric_date = serializers.DateField(
        format=settings.REST_DATE_FORMAT,
        input_formats=[settings.REST_DATE_FORMAT, 'iso-8601'],
    )
    channel = serializers.CharField()
    country = serializers.CharField()
    operating_system = serializers.CharField()

    impressions_count_total = serializers.IntegerField()
    clicks_count_total = serializers.IntegerField()
    installations_count_total = serializers.IntegerField()
    spend_money_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    revenue_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    cpi_total = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        fields = [
            'metric_date',
            'channel',
            'country',
            'operating_system',
            'impressions_count_total',
            'clicks_count_total',
            'installations_count_total',
            'spend_money_total',
            'revenue_total',
            'cpi_total',
        ]

    def get_fields(self):
        fields = super().get_fields()

        groupby = self.context['request'].query_params.get('groupby')
        if not groupby:
            return fields

        filtered_fields = {i for i in fields if i not in self.allowed_groupings or i in groupby.split(',')}
        return {k: v for k, v in fields.items() if k in filtered_fields}
