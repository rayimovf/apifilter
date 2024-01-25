from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from . import models
from . import serializer


class GetClient(ListAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializer.ClientSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'is_active']
    search_fields = ['first_name']

