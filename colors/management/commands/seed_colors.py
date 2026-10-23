from django.core.management.base import BaseCommand
from colors.models import Color

COLORS = [
    ("Red", "#FF0000"),
    ("Green", "#008000"),
    ("Blue", "#0000FF"),
    ("Yellow", "#FFFF00"),
    ("Orange", "#FFA500"),
    ("Purple", "#800080"),
    ("Pink", "#FFC0CB"),
    ("Black", "#000000"),
    ("White", "#FFFFFF"),
    ("Gray", "#808080"),
]


class Command(BaseCommand):
    help = "Seed the database with 10 starter colors"

    def handle(self, *args, **options):
        for name, hex_code in COLORS:
            Color.objects.get_or_create(name=name, defaults={"hex_code": hex_code})
        self.stdout.write(self.style.SUCCESS("Seeded colors"))