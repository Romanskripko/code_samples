from rest_framework import serializers
from core.serializers import DefaultModelSerializer, default_serializer
from rest_framework.exceptions import ValidationError

from .models import Dot, DotCloud, CoordinatesField, Line
from drf_writable_nested.serializers import WritableNestedModelSerializer


@default_serializer(CoordinatesField)
class CoordinatesSerializerField(serializers.JSONField):
    """changes data read and write behavior just in case to show that decorator works
        yes, swagger won't understand the idea natively but that's not the target"""
    def to_representation(self, value):
        return f'({value["x"]}, {value["y"]})'

    def to_internal_value(self, data):
        if not isinstance(data, list):
            msg = 'Incorrect type. Expected a list, but got %s'
            raise ValidationError(msg % type(data).__name__)
        elif len(data) != 2:
            msg = 'Incorrect length. Expected exactly 2 items, but got %s'
            raise ValidationError(msg % len(data))
        elif not all(isinstance(item, (int, float)) for item in data):
            msg = 'Incorrect items type. Ensure that all items are int or float'
            raise ValidationError(msg)
        return {'x': data[0], 'y': data[1]}


@default_serializer
class DotSerializer(DefaultModelSerializer):
    class Meta:
        model = Dot
        fields = ('id', 'coords')


class DotCloudSerializer(WritableNestedModelSerializer, DefaultModelSerializer):
    """Short and simple CRUD ready serializer for dotclouds"""
    class Meta:
        model = DotCloud
        fields = ('id', 'name', 'equation', 'dots', 'dots_quantity')


class LinesSerializer(DefaultModelSerializer):
    class Meta:
        model = Line
        fields = ('id', 'start', 'end', 'length')
