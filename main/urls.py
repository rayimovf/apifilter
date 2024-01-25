from django.urls import path
from . import views

urlpatterns = [
    path('get-teachers/', views.GetTeachers.as_view()),
    path('get-students/', views.GetStudents.as_view()),
    path('get-teacher/', views.GetGroup.as_view()),
]