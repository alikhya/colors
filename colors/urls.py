from django.urls import path
from .views import ColorListView

urlpatterns = [
    path("colors/", ColorListView.as_view(), name="color-list"),
]