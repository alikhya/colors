from rest_framework.generics import ListCreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.throttling import ScopedRateThrottle

from .models import Color
from .serializers import ColorSerializer

class ColorListView(ListCreateAPIView):
    queryset = Color.objects.all().order_by("id")
    serializer_class = ColorSerializer


class LoginView(ObtainAuthToken):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "login"