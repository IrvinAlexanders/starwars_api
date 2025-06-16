import strawberry

from core.models import Character
from core.graphql.types import FilmType


@strawberry.django.type(Character)
class CharacterType:
    """Represents a character from the Star Wars universe.

    Attributes:
        id (ID): The unique identifier of the character.
        name (str): The name of the character.
        birth_year (str | None): The birth year of the character, can be
        gener (str | None): The gender of the character, can be blank or null.
        films (list[FilmType]): The films in which this character appears, represented as a
        list of FilmType objects.
    """

    id: strawberry.ID
    name: str
    birth_year: str | None
    gender: str | None
    films: list[FilmType]