from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from . import models
from . import serializer


class GetGroup(ListAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializer.GroupSerializer


class GetTeachers(ListAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = serializer.TeacherSerializer


class GetStudents(ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['group', 'teacher']
    search_fields = ['last_name']

