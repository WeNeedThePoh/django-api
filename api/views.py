from rest_framework import viewsets
from api.serializers import OccurenceSerializer
from api.models import Occurence

class OccurenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows occurences to be viewed or edited.
    """
    queryset = Occurence.objects.all()
    serializer_class = OccurenceSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Occurence.objects.all()
        type = self.request.query_params.get('type', None)
        filter = self.request.query_params.get('filter', None)

        if type is not None:
            if type == 'author':
                queryset = queryset.filter(author__iexact=filter)
            elif type == 'category':
                queryset = queryset.filter(category__iexact=filter)
            else:
                queryset = queryset.filter(status__iexact=filter)
        return queryset
