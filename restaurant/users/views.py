from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, Employee
from .serializers import RegisterUserSerializer, UserSerializer, EmployeerSerializer


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        request_data = request.data
        serializer = RegisterUserSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Incorrect input.'}, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'You are logged out.'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class EmployeeView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeerSerializer(employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateEmployeeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = EmployeerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
