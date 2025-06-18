from django.core.management.base import BaseCommand
from core.models import Character, Film, Planet


class Command(BaseCommand):
    help = "Seed database with Star Wars sample data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")

        # Clean up
        Character.objects.all().delete()
        Film.objects.all().delete()
        Planet.objects.all().delete()

        # Planets
        tatooine = Planet.objects.create(name="Tatooine", climate="arid", population=200000)
        alderaan = Planet.objects.create(name="Alderaan", climate="temperate", population=2000000)

        # Characters
        luke = Character.objects.create(name="Luke Skywalker", birth_year="19BBY", gender="male")
        leia = Character.objects.create(name="Leia Organa", birth_year="19BBY", gender="female")

        # Films
        new_hope = Film.objects.create(
            title="A New Hope",
            episode_id=4,
            opening_crawl="It is a period of civil war...",
            director="George Lucas",
            producers="Gary Kurtz, Rick McCallum",
            release_date="1977-05-25"
        )
        new_hope.characters.set([luke, leia])
        new_hope.planets.set([tatooine, alderaan])

        self.stdout.write(self.style.SUCCESS("✅ Database seeded successfully!"))