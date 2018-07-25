from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from api import views

router = routers.DefaultRouter()
router.register(r'occurences', views.OccurenceViewSet)

slashless_router = routers.DefaultRouter(trailing_slash=False)
slashless_router.registry = router.registry[:]

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(slashless_router.urls)),
]
