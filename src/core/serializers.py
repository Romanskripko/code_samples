from rest_framework import serializers
from rest_framework.utils.field_mapping import get_relation_kwargs


class DefaultModelSerializer(serializers.ModelSerializer):
    """ ModelSerializer with extendable field mapping for nested serialization and custom fields """
    serializer_field_mapping = serializers.ModelSerializer.serializer_field_mapping
    serializer_related_field_mapping = {}

    def build_relational_field(self, field_name, relation_info):
        field_kwargs = get_relation_kwargs(field_name, relation_info)
        if relation_info.related_model in self.serializer_related_field_mapping:
            field_class = self.serializer_related_field_mapping[relation_info.related_model]
            field_kwargs.pop('queryset')
            field_kwargs.pop('to_field')
            field_kwargs.pop('view_name', None)
            return field_class, field_kwargs
        return super(DefaultModelSerializer, self).build_relational_field(field_name, relation_info)


def default_serializer(serializer_cls=None):
    """ Decorator with optional param for DefaultModelSerializer fields mapping
        param provides custom field, for nested serializers param is not used"""
    field_class = None

    def _decorate(cls):
        if issubclass(cls, serializers.ModelSerializer) and field_class is None:
            DefaultModelSerializer.serializer_related_field_mapping[cls.Meta.model] = cls
            return cls
        elif field_class is None:
            raise Exception('Please enter a field name or use ModelSerializer')
        DefaultModelSerializer.serializer_field_mapping[field_class] = cls
        return cls
    if serializer_cls and issubclass(serializer_cls, serializers.ModelSerializer):
        return _decorate(serializer_cls)
    elif serializer_cls:
        field_class = serializer_cls
        return _decorate
    return _decorate
