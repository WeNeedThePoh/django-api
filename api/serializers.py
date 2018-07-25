from rest_framework import serializers
from api.models import Occurence

class OccurenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Occurence
        fields = ('id', 'author', 'description', 'createdData', 'updatedDate', 'category', 'status')
