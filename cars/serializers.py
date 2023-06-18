# cars/serializers.py

from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'car_brand', 'release_year', 'seats', 'body_type', 'engine_volume']