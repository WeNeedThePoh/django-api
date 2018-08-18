from __future__ import unicode_literals
from django.contrib.gis.db import models


class Occurence(models.Model):
    CATEGORIES = (
        ('CONSTRUCTION', 'CONSTRUCTION'),
        ('SPECIAL_EVENT', 'SPECIAL_EVENT'),
        ('INCIDENT', 'INCIDENT'),
        ('WEATHER_CONDITION', 'WEATHER_CONDITION'),
        ('ROAD_CONDITION', 'ROAD_CONDITION'),
    )

    STATUS = (
        ('To_be_validated', 'To be validated'),
        ('Validated', 'Validated'),
        ('Solved', 'Solved'),
    )

    author = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    createdData = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    position = models.PointField(null=True, blank=True)
    category = models.CharField(max_length=255, choices=CATEGORIES, null=False)
    status = models.CharField(max_length=255, choices=STATUS, null=False, default='To be validated')

    def __str__(self):
        return "{} - {} - {} - {} - {} - {}".format(self.author, self.description, self.createdData, self.updatedDate, self.position, self.category, self.status)
