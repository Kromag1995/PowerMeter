from rest_framework import serializers
from base.models import Wattmeter, Measure


class WattmeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wattmeter
        fields = ["name", "unkey"]


class MeasureSerializer(serializers.ModelSerializer):
    # DRF doesn't have positive field, so I use Integer with 0 min
    value = serializers.IntegerField(min_value=0)

    class Meta:
        model = Measure
        fields = ["created", "value", "wattmeter"]
