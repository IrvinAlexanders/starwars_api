import strawberry

from core.models import Film
from core.graphql.types import PlanetType


@strawberry.django.type(Film)
class FilmType:
    """Represents a Star Wars film.
    Attributes:
        id (ID): The unique identifier of the film.
        title (str): The title of the film.
        episode_id (int): The episode number of the film.
        opening_crawl (str): The opening crawl text shown at the beginning of the film.
        director (str): The name of the film's director.
        producers (str): A comma-separated list of the film's producers.
        release_date (str): The release date of the film.
        planets (list[PlanetType]): The planets featured in the film, represented as a list of PlanetType objects.
    """

    id: strawberry.ID
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producers: str
    release_date: str
    planets: list[PlanetType]