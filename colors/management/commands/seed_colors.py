from django.core.management.base import BaseCommand
from colors.models import Color

COLORS = [
    # original 10
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
    # 30 new
    ("Maroon", "#800000"),
    ("Crimson", "#DC143C"),
    ("Coral", "#FF7F50"),
    ("Salmon", "#FA8072"),
    ("Gold", "#FFD700"),
    ("Khaki", "#F0E68C"),
    ("Lime", "#00FF00"),
    ("Olive", "#808000"),
    ("Teal", "#008080"),
    ("Cyan", "#00FFFF"),
    ("Turquoise", "#40E0D0"),
    ("Navy", "#000080"),
    ("Indigo", "#4B0082"),
    ("Violet", "#EE82EE"),
    ("Magenta", "#FF00FF"),
    ("Lavender", "#E6E6FA"),
    ("Brown", "#A52A2A"),
    ("Chocolate", "#D2691E"),
    ("Tan", "#D2B48C"),
    ("Beige", "#F5F5DC"),
    ("Ivory", "#FFFFF0"),
    ("Silver", "#C0C0C0"),
    ("Charcoal", "#36454F"),
    ("Mint", "#98FF98"),
    ("Peach", "#FFDAB9"),
    ("Sky Blue", "#87CEEB"),
    ("Rose", "#FF007F"),
    ("Plum", "#8E4585"),
    ("Amber", "#FFBF00"),
    ("Emerald", "#50C878"),
]


class Command(BaseCommand):
    help = "Seed the database with 10 starter colors"

    def handle(self, *args, **options):
        for name, hex_code in COLORS:
            Color.objects.get_or_create(name=name, defaults={"hex_code": hex_code})
        self.stdout.write(self.style.SUCCESS("Seeded colors"))