import strawberry
from strawberry.relay import Node
from typing import Optional, ForwardRef

from core.models import Character, Film, Planet


FilmTypeRef = ForwardRef("FilmType")


@strawberry.django.type(Planet)
class PlanetType(Node):
    """Represents a planet in the Star Wars universe.

    Attributes:
        id (ID): The unique identifier of the planet.
        name (str): The name of the planet.
        climate (str | None): The climate of the planet, can be blank or null.
        terrain (str | None): The terrain of the planet, can be blank or null.
        population (str | None): The population of the planet, can be blank or null.
    """
    name: str = strawberry.field(description="The name of the planet.")
    climate: str | None = strawberry.field(
        description="The climate of the planet, can be blank or null."
    )
    terrain: str | None = strawberry.field(
        description="The terrain of the planet, can be blank or null."
    )
    population: str | None = strawberry.field(
        description="The population of the planet, can be blank or null."
    )


@strawberry.django.type(Film)
class FilmType(Node):
    """Represents a Star Wars film.
    Attributes:
        id (ID): The unique identifier of the film.
        title (str): The title of the film.
        episode_id (int): The episode number of the film.
        opening_crawl (str): The opening crawl text shown at the beginning of the film.
        director (str): The name of the film's director.
        producers (str): A comma-separated list of the film's producers.
        release_date (str): The release date of the film.
        planets (list[PlanetType]): The planets featured in the film,
        represented as a list of PlanetType objects.
    """
    title: str = strawberry.field(description="The title of the film.")
    episode_id: int = strawberry.field(description="The episode number of the film.")
    opening_crawl: str = strawberry.field(
        description="The opening crawl text shown at the beginning of the film."
    )
    director: str = strawberry.field(description="The name of the film's director.")
    producers: str = strawberry.field(
        description="A comma-separated list of the film's producers."
    )
    release_date: str = strawberry.field(description="The release date of the film.")

    @strawberry.django.field(description="The planets featured in the film.")
    def planets(self) -> list["PlanetType"]:
        return self.planets.all()


@strawberry.django.type(Character)
class CharacterType(Node):
    """Represents a character from the Star Wars universe.

    Attributes:
        id (ID): The unique identifier of the character.
        name (str): The name of the character.
        birth_year (str | None): The birth year of the character, can be
        gender (str | None): The gender of the character, can be blank or null.
        films (list[FilmType]): The films in which this character appears,
        represented as a
        list of FilmType objects.
    """
    name: str = strawberry.field(description="The name of the character.")
    birth_year: Optional[str] = strawberry.field(
        description="The birth year of the character, can be blank or null."
    )
    gender: Optional[str] = strawberry.field(
        description="The gender of the character, can be blank or null."
    )

    @strawberry.django.field(
        description="Returns the films in which this character appears."
    )
    def films(self) -> list["FilmType"]:
        """Returns the films in which this character appears."""
        return self.films.all()
