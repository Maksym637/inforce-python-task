from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from users.views import RegisterView, BlacklistTokenView, UserView, EmployeeView
from place.views import CreateRestaurantView, RestaurantView
from menus.views import CreateMenuView, MenuView, CreateVoteView, VoteView


urlpatterns = [
    # authorization and authentication :
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='create_user'),
    path('logout/', BlacklistTokenView.as_view(), name='blacklist'),
    path('admin/', admin.site.urls),

    # users :
    path('users/', UserView.as_view(), name='users'),

    # employees :
    path('employees/', EmployeeView.as_view(), name='employee'),

    # restaurants :
    path('restaurant/create/', CreateRestaurantView.as_view(), name='create_restaurant'),
    path('restaurants/', RestaurantView.as_view(), name='restaurants'),

    # menus :
    path('menu/create/', CreateMenuView.as_view(), name='create_menu'),
    path('menus/', MenuView.as_view(), name='menus'),

    # votes :
    path('vote/create/', CreateVoteView.as_view(), name='create_vote'),
    path('votes/', VoteView.as_view(), name='votes'),
]
