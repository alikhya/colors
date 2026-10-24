from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle, ScopedRateThrottle

from .models import Color
from .serializers import ColorSerializer


# ---------- Management API (Chapters 1-5) ----------
class ColorListView(ListCreateAPIView):
    queryset = Color.objects.all().order_by("id")
    serializer_class = ColorSerializer


class LoginView(ObtainAuthToken):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "login"


# ---------- Public API (Chapter 6) ----------
class PublicRateThrottle(AnonRateThrottle):
    scope = "public"


class PublicColorMixin:
    queryset = Color.objects.all().order_by("id")
    serializer_class = ColorSerializer
    authentication_classes = []          # ignore tokens and sessions entirely
    permission_classes = [AllowAny]      # no login needed
    throttle_classes = [PublicRateThrottle]


class PublicColorListView(PublicColorMixin, ListAPIView):
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "hex_code"]
    ordering_fields = ["id", "name"]
    ordering = ["id"]


class PublicColorDetailView(PublicColorMixin, RetrieveAPIView):
    pass