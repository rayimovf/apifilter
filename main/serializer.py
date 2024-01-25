from rest_framework import serializers
from . import models


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Group
        fields = '__all__'
