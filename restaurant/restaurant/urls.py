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
    path('users_list/', UserView.as_view(), name='users'),

    # employees :
    path('employee/', EmployeeView.as_view(), name='employee'),

    # restaurants :
    path('restaurant/', CreateRestaurantView.as_view(), name='create_restaurant'),
    path('restaurants_list/', RestaurantView.as_view(), name='restaurants'),

    # menus :
    path('menu/', CreateMenuView.as_view(), name='create_menu'),
    path('menus_list/', MenuView.as_view(), name='menus'),

    # votes :
    path('vote/', CreateVoteView.as_view(), name='create_vote'),
    path('votes_list/', VoteView.as_view(), name='votes'),

    # results :

]
