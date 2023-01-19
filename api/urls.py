from django.urls import path, include
from rest_framework import routers
from .views import WattmeterViewSet, MeasureViewSet

router = routers.DefaultRouter()
router.register(r"wattmeter", WattmeterViewSet, basename="wattmeter")
router.register(r"measure", MeasureViewSet, basename="measure")


urlpatterns = [
    path("", include(router.urls))
]