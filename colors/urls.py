from django.urls import path
from .views import ColorListView, LoginView

urlpatterns = [
    path("colors/", ColorListView.as_view(), name="color-list"),
    path("token/", LoginView.as_view(), name="api-token"),
]