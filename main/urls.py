from django.urls import path
from . import views

urlpatterns = [
    path('get-client/', views.GetClient.as_view()),
]