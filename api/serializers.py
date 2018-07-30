from rest_framework import serializers
from api.models import Occurence

class OccurenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurence
        fields = ('id', 'author', 'description', 'createdData', 'updatedDate', 'position', 'category', 'status')
