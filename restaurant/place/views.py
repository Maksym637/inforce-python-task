from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Restaurant
from .serializers import RestaurantSerializer


class CreateRestaurantView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format=None):
        request_data = request.data
        serializer = RestaurantSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Incorrect input.'}, status=status.HTTP_400_BAD_REQUEST)


class RestaurantView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        restaurant = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
