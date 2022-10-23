from django.db.models import Q
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Menu, Vote
from .serializers import MenuSerializer, VoteSerializer


class CreateMenuView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        request_data = request.data
        serializer = MenuSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Incorrect input.'}, status=status.HTTP_400_BAD_REQUEST)


class MenuView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        todays_date = settings.CURRENT_DATE.date()
        qs = Menu.objects.filter(Q(created_at__date=todays_date))
        serializer = MenuSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateVoteView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(elf, request, format=None):
        request_data = request.data
        serializer = VoteSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Incorrect input.'}, status=status.HTTP_400_BAD_REQUEST)


class VoteView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        employee = Vote.objects.all()
        serializer = VoteSerializer(employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
