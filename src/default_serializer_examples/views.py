from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import serializers, models


class DotsViewSet(ModelViewSet):
    queryset = models.Dot.objects.all()
    serializer_class = serializers.DotSerializer


class DotCloudViewSet(ModelViewSet):
    queryset = models.DotCloud.objects.all().prefetch_related('dots')
    serializer_class = serializers.DotCloudSerializer


class LinesViewSet(ModelViewSet):
    queryset = models.Line.objects.all()
    serializer_class = serializers.LinesSerializer
