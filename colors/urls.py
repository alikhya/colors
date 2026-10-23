from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ColorListView

urlpatterns = [
    path("colors/", ColorListView.as_view(), name="color-list"),
    path("token/", obtain_auth_token, name="api-token"),
]