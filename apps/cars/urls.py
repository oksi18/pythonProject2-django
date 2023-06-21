from django.urls import path

from apps.cars.views import CarListView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('cars/', CarListView.as_view()),
    path('cars/<int:pk>/', CarRetrieveUpdateDestroyView.as_view()),
]