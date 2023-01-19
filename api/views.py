from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from django.db.models import Max, Min, Avg, Sum

from base.models import Wattmeter, Measure
from .serializers import WattmeterSerializer, MeasureSerializer


class WattmeterViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Wattmeter.objects.all()
    serializer_class = WattmeterSerializer

    @action(methods=['GET'], detail=True)
    def max_consume(self, request, pk):
        return Response(Measure.objects.filter(wattmeter=pk).aggregate(Max('value')))

    @action(methods=['GET'], detail=True)
    def min_consume(self, request, pk):
        return Response(Measure.objects.filter(wattmeter=pk).aggregate(Min('value')))

    @action(methods=['GET'], detail=True)
    def total_consume(self, request, pk):
        return Response(Measure.objects.filter(wattmeter=pk).aggregate(Sum('value')))

    @action(methods=['GET'], detail=True)
    def mean_consume(self, request, pk):
        return Response(Measure.objects.filter(wattmeter=pk).aggregate(Avg('value')))


class MeasureViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer


