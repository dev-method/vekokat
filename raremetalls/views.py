# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from raremetalls.models import PlatinumPrice, TantalPrice, RhodyiPrice
from raremetalls.serializers import RhodyiSerializer, TantalSerializer, PlatinumSerializer

# Create your views here.
@api_view(['GET'])
def platinum_api(request):
    if request.method == 'GET':
        prices = PlatinumPrice.objects.all()
        serializer = PlatinumSerializer(prices, many=True)
        return Response(serializer.data)
@api_view(['GET'])
def palladium_api(request):
    if request.method == 'GET':
        prices = TantalPrice.objects.all()
        serializer = TantalSerializer(prices, many=True)
        return Response(serializer.data)
@api_view(['GET'])
def rhodyi_api(request):
    if request.method == 'GET':
        prices = RhodyiPrice.objects.all()
        serializer = RhodyiSerializer(prices, many=True)
        return Response(serializer.data)
