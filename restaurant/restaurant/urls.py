from django.contrib import admin
from django.urls import path, re_path

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from users.views import RegisterView, LogoutView, UserView, EmployeeView, CreateEmployeeView
from place.views import CreateRestaurantView, RestaurantView
from menus.views import CreateMenuView, MenuView, CreateVoteView, VoteView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # get documentation with swagger :
    # swagger path = swagger/
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # authorization and authentication :
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='create_user'),
    path('logout/', LogoutView.as_view(), name='blacklist'),
    path('admin/', admin.site.urls),

    # users :
    path('user/', UserView.as_view(), name='users'),

    # employees :
    path('employee/create/', CreateEmployeeView.as_view(), name='create_employee'),
    path('employee/', EmployeeView.as_view(), name='employees'),

    # restaurants :
    path('restaurant/create/', CreateRestaurantView.as_view(), name='create_restaurant'),
    path('restaurant/', RestaurantView.as_view(), name='restaurants'),

    # menus :
    path('menu/create/', CreateMenuView.as_view(), name='create_menu'),
    path('menu/', MenuView.as_view(), name='menus'),

    # votes :
    path('vote/create/', CreateVoteView.as_view(), name='create_vote'),
    path('vote/', VoteView.as_view(), name='votes'),
]
