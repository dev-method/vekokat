from raremetalls.models import PlatinumPrice, RhodyiPrice, TantalPrice
from rest_framework import serializers

class PlatinumSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatinumPrice
        fields = ('price_rb', 'price_dl', 'price_eu')

class TantalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TantalPrice
        fields = ('price_rb', 'price_dl', 'price_eu')

class RhodyiSerializer(serializers.ModelSerializer):
    class Meta:
        model = RhodyiPrice
        fields = ('price_rb', 'price_dl', 'price_eu')