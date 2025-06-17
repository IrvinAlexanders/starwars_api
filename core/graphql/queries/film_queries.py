import strawberry
from strawberry.relay import Connection
from typing import List

from core.models import Film
from core.graphql.types import FilmType


@strawberry.type
class FilmQueries:
    """Queries for retrieving films from the Star Wars universe.
    """
    @strawberry.django.field
    def films(self) -> Connection[FilmType]:
        return Connection.from_queryset(Film.objects.all())
