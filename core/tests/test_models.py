from core.tests.base import SWAPITestCase
from core.models import Film, Planet, Character


class FilmModelTest(SWAPITestCase):
    def setUp(self):
        # Arrange
        self.film = Film.objects.create(
            title="A New Hope",
            episode_id=4,
            opening_crawl="It is a period of civil war...",
            director="George Lucas",
            producers="Gary Kurtz, Rick McCallum",
            release_date="1977-05-25"
        )

    def test_film_creation(self):
        # Act & Assert
        self.assertEqual(self.film.title, "A New Hope")
        self.assertEqual(self.film.episode_id, 4)
        self.assertEqual(self.film.director, "George Lucas")
        self.assertEqual(self.film.release_date, "1977-05-25")

    def test_film_str(self):
        # Act & Assert
        self.assertEqual(str(self.film), "Episode 4: A New Hope")


class PlanetModelTest(SWAPITestCase):
    def setUp(self):
        # Arrange
        self.planet = Planet.objects.create(
            name="Tatooine",
            climate="arid",
            terrain="desert",
            population=200000
        )

    def test_planet_creation(self):
        # Act & Assert
        self.assertEqual(self.planet.name, "Tatooine")
        self.assertEqual(self.planet.climate, "arid")
        self.assertEqual(self.planet.terrain, "desert")
        self.assertEqual(self.planet.population, 200000)

    def test_planet_str(self):
        # Act & Assert
        self.assertEqual(str(self.planet), "Tatooine")


class CharacterModelTest(SWAPITestCase):
    def setUp(self):
        # Arrange
        self.character = Character.objects.create(
            name="Luke Skywalker",
            birth_year="19BBY",
            gender="male"
        )
        self.film = Film.objects.create(
            title="A New Hope",
            episode_id=4,
            opening_crawl="It is a period of civil war...",
            director="George Lucas",
            producers="Gary Kurtz, Rick McCallum",
            release_date="1977-05-25"
        )
        self.character.films.add(self.film)

    def test_character_creation(self):
        # Act & Assert
        self.assertEqual(self.character.name, "Luke Skywalker")
        self.assertEqual(self.character.birth_year, "19BBY")
        self.assertEqual(self.character.gender, "male")
        self.assertIn(self.film, self.character.films.all())

    def test_character_str(self):
        # Act & Assert
        self.assertEqual(str(self.character), "Luke Skywalker")