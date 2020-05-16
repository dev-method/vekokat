from core.models import NewAdvantages, NewWorkingMethods, NewLaboratory, NewRegions, NewPriceBlock
from rest_framework import serializers

class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewAdvantages
        fields = ('icon_image', 'text','group')

class WorkingMethodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewWorkingMethods
        fields = ('number', 'text','image','group')

class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewLaboratory
        fields = ('title', 'icon_image','text','group')

class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewRegions
        fields = ('icon_image','text','group')

class PriceBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewPriceBlock
        fields = ('image','title','text', 'price', 'group')