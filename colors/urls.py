from django.urls import path
from .views import (
    ColorListView,
    LoginView,
    PublicColorListView,
    PublicColorDetailView,
)

urlpatterns = [
    # management
    path("colors/", ColorListView.as_view(), name="color-list"),
    path("token/", LoginView.as_view(), name="api-token"),
    # public
    path("public/colors/", PublicColorListView.as_view(), name="public-color-list"),
    path("public/colors/<int:pk>/", PublicColorDetailView.as_view(), name="public-color-detail"),
]