from django.urls import path
from todoomatic.users.api.views import UserList, current_user

from todoomatic.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

from rest_framework_jwt.views import obtain_jwt_token

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("token/", obtain_jwt_token),
    path("current_user/", current_user),
    path("list/", UserList.as_view(), name="user_list"),
]
