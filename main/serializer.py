from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Client
        fields = '__all__'

