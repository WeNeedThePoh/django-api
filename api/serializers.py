from rest_framework import serializers
from api.models import Occurence
from django.contrib.gis.geos import GEOSGeometry

class OccurenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurence
        geometry_field= 'point'
        fields = ('id', 'author', 'description', 'createdData', 'updatedDate', 'position', 'category', 'status')
