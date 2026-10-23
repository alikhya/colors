import re
from rest_framework import serializers
from .models import Color

HEX_PATTERN = re.compile(r"^#[0-9A-Fa-f]{6}$")


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["id", "name", "hex_code"]

    def validate_hex_code(self, value):
        if not HEX_PATTERN.match(value):
            raise serializers.ValidationError(
                "Hex code must look like #RRGGBB, for example #FF5733."
            )
        return value.upper()

    def validate_name(self, value):
        value = value.strip()
        if Color.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("A color with this name already exists.")
        return value