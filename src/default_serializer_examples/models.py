from math import sqrt

from django.db import models


class CoordinatesField(models.JSONField):
    """ Fake Custom Field for default_serializer testing """
    description = 'XY coordinates field'


class DotCloud(models.Model):
    name = models.CharField(max_length=100)
    equation = models.CharField(max_length=100)

    @property
    def dots_quantity(self):
        return self.dots.count()


class Line(models.Model):
    start = CoordinatesField()
    end = CoordinatesField()

    @property
    def length(self):
        ret = sqrt((self.start['x'] - self.end['x']) ** 2 + (self.start['y'] - self.end['y']) ** 2)
        return ret


class Dot(models.Model):
    cloud = models.ForeignKey(DotCloud, on_delete=models.CASCADE, related_name='dots', null=True, blank=True)
    coords = CoordinatesField()
