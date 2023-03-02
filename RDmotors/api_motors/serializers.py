from rest_framework import serializers

from mainapp.models import PartCard, Category, Cars, Photo


class CategoryDetailSerializer(serializers.ModelSerializer):
    """Описание категории"""
    class Meta:
        model = Category
        fields = '__all__'


class CarDetailSerializer(serializers.ModelSerializer):
    """Описание автомобиля"""
    class Meta:
        model = Cars
        fields = '__all__'


class PhotoDetailSerializer(serializers.ModelSerializer):
    """Описание фото"""

    class Meta:
        model = Photo
        fields = '__all__'


class PartCardListSerializer(serializers.ModelSerializer):
    """Список запчастей"""
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    car = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = PartCard
        fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
    """Список категорий"""
    class Meta:
        model = Category
        fields = '__all__'


class PartCardDetailSerializer(serializers.ModelSerializer):
    """Описание запчасти"""
    category = CategoryDetailSerializer()
    car = CarDetailSerializer()
    image = PhotoDetailSerializer(many=True)

    class Meta:
        model = PartCard
        fields = '__all__'


class CarsListSerializer(serializers.ModelSerializer):
    """Список автомобилей"""
    class Meta:
        model = Cars
        fields = '__all__'
