from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import CarModel
from .serializers import CarSerializer
from .filters import car_filtered_queryset


# class CarListView(ListAPIView):
#     def get_queryset(self):
#         return car_filtered_queryset(self.request.query_params)

class CarListView(generics.ListCreateAPIView):
    serializer_class = CarSerializer  # Define your serializer class here

    def get_queryset(self):
        return car_filtered_queryset(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()