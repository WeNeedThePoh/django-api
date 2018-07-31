from rest_framework import viewsets
from api.serializers import OccurenceSerializer
from api.models import Occurence
from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import GEOSGeometry
from decimal import Decimal

class OccurenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows occurences to be viewed or edited.
    """
    queryset = Occurence.objects.all()
    serializer_class = OccurenceSerializer

    def get_queryset(self):
        """
        Filtering occurences by status, author, category or distance
        """
        queryset = Occurence.objects.all()
        author = self.request.query_params.get('author', '')
        category = self.request.query_params.get('category', '')
        status = self.request.query_params.get('status', '')
        lng = self.request.query_params.get('lng', None)
        lat = self.request.query_params.get('lat', None)
        distance = self.request.query_params.get('distance', None)

        locationFilter = createPointFromLocation(lng, lat, distance)

        if locationFilter is not None:
            queryset = queryset.filter(
                author__icontains=author,
                category__icontains=category,
                status__icontains=status,
                position__distance_lte=(
                    locationFilter[0],
                    locationFilter[1]
                )
            )

        queryset = queryset.filter(
            author__icontains=author,
            category__icontains=category,
            status__icontains=status
        )

        return queryset

def createPointFromLocation(lng, lat, distance):
    if all([lng, lat, distance]):
        longitude = Decimal(lng)
        latitude = Decimal(lat)

        point = GEOSGeometry("POINT({} {})".format(longitude, latitude))
        radius = Distance(km=distance)

        return [point, radius]
    else:
        return None
