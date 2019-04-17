from django.db.models import DecimalField, Sum
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter

from .filters import MetricsFilter
from .models import AdvertisementMetric
from .serializers import GroupedMetricSerializer, MetricSerializer


class MetricsViewSet(viewsets.ModelViewSet):
    queryset = AdvertisementMetric.objects.all()

    serializer_class = MetricSerializer

    filterset_class = MetricsFilter
    filter_backends = viewsets.ModelViewSet.filter_backends + [OrderingFilter]


class GroupedMetricsView(generics.ListAPIView):
    serializer_class = GroupedMetricSerializer

    filterset_class = MetricsFilter
    filter_backends = viewsets.ModelViewSet.filter_backends + [OrderingFilter]

    def get_queryset(self):
        group_by = self.request.query_params.get('groupby')
        if not group_by:
            return self.get_queryset_with_annotations(GroupedMetricSerializer.allowed_groupings)

        group_by_fields = group_by.split(',')
        if not GroupedMetricSerializer.allowed_groupings.issuperset(group_by_fields):
            return AdvertisementMetric.objects.none()

        return self.get_queryset_with_annotations(group_by_fields)

    @staticmethod
    def get_queryset_with_annotations(group_by_fields):
        return AdvertisementMetric.objects.values(*group_by_fields).annotate(
            impressions_count_total=Sum('impressions_count'),
            clicks_count_total=Sum('clicks_count'),
            installations_count_total=Sum('installations_count'),
            spend_money_total=Sum('spend_money'),
            revenue_total=Sum('revenue'),
            cpi_total=(
                Sum('spend_money', output_field=DecimalField()) /
                Sum('installations_count', output_field=DecimalField())
            ),
        )
