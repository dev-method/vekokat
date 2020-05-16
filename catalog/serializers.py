from catalog.models import AutoCatalog
from rest_framework import serializers

class AutoCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoCatalog
        fields = ('id', 'auto_model', 'year','weight', 'price_kg', 'sum', 'category')