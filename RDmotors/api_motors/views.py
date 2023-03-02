from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from mainapp.models import PartCard, Category, Cars, Photo
from . import serializers


class PartCardListView(generics.ListAPIView):
    """Вывод списка запчастей"""
    queryset = PartCard.objects.all()
    serializer_class = serializers.PartCardListSerializer


class CategoryListView(generics.ListAPIView):
    """Вывод списка запчастей"""
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryListSerializer


class PartCardDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Вывод запчасти"""
    queryset = PartCard.objects
    serializer_class = serializers.PartCardDetailSerializer


class CarsListView(generics.ListAPIView):
    """Вывод списка автомобилей"""
    queryset = Cars.objects.all()
    serializer_class = serializers.CarsListSerializer
