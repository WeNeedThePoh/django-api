from rest_framework import viewsets
from api.serializers import OccurenceSerializer
from api.models import Occurence

class OccurenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows occurences to be viewed or edited.
    """
    queryset = Occurence.objects.all()
    serializer_class = OccurenceSerializer
