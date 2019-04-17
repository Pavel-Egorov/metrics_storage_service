from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'metrics', views.MetricsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('grouped_metrics/', views.GroupedMetricsView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
