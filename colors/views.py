from rest_framework.generics import ListCreateAPIView
from .models import Color
from .serializers import ColorSerializer


class ColorListView(ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer