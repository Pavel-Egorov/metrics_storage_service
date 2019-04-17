from django.contrib import admin


class AdvertisementMetricAdmin(admin.ModelAdmin):
    fieldsets = [
        [None, {'fields': [
            'metric_date',
            'channel',
            'country',
            'operating_system',
            'impressions_count',
            'clicks_count',
            'installations_count',
        ]}],
        ['money', {'fields': [
            'spend_money',
            'revenue',
            'cpi',
        ]}],
    ]
    readonly_fields = ['cpi']

    list_display = [
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
    list_filter = ['channel', 'country', 'operating_system']
    search_fields = ['channel', 'country', 'operating_system']

    ordering = ['metric_date']
    date_hierarchy = 'metric_date'
