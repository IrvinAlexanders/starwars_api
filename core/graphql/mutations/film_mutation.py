import strawberry

from core.models import Film, Planet, Character
from core.graphql.types import FilmType


@strawberry.input
class CreateFilmInput:
    """Input type for creating a new film in the Star Wars universe.
    This class contains fields required to create a film, including title,
    opening crawl, director, producers, and optional character and planet IDs.
    """
    title: str = strawberry.field(
        description="The title of the film."
    )
    opening_crawl: str = strawberry.field(
        description="The opening crawl text shown at the beginning of the film."
    )
    director: str = strawberry.field(
        description="The name of the film's director."
    )
    episode_id: int = strawberry.field(
        description="The episode number of the film."
    )
    producers: str = strawberry.field(
        description="A comma-separated list of the film's producers."
    )
    release_date: str = strawberry.field(
        description="The release date of the film in YYYY-MM-DD format."
    )
    character_ids: list[int] = strawberry.field(
        default_factory=list,
        description="List of character IDs associated with the film."
    )
    planet_ids: list[int] = strawberry.field(
        default_factory=list,
        description="List of planet IDs associated with the film."
    )


@strawberry.type
class FilmMutations:
    """Mutations for creating and updating films in the Star Wars universe.
    This class contains methods for creating a new film.
    """
    @strawberry.mutation
    def create_film(self, input: CreateFilmInput) -> FilmType:
        film = Film.objects.create(
            title=input.title,
            episode_id=input.episode_id,
            opening_crawl=input.opening_crawl,
            director=input.director,
            producers=input.producers,
            release_date=input.release_date
        )
        if input.character_ids:
            film.characters.set(Character.objects.filter(id__in=input.character_ids))
        if input.planet_ids:
            film.planets.set(Planet.objects.filter(id__in=input.planet_ids))
        return film
