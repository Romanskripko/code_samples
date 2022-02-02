from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'dots', views.DotsViewSet, basename='dots')
router.register(r'clouds', views.DotCloudViewSet, basename='clouds')
router.register(r'lines', views.LinesViewSet, basename='lines')

urlpatterns = [
    path('', include(router.urls)),
]
