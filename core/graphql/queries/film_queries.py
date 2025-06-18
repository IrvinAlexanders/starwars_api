import strawberry
from strawberry import relay
from typing import List, Iterable

from core.models import Film
from core.graphql.types import FilmType


@strawberry.type
class FilmQueries:
    """Queries for retrieving films from the Star Wars universe.
    """
    @relay.connection(
        relay.ListConnection[FilmType],
        description="Retrieve a list of films from the Star Wars universe."
    )
    def films(self) -> Iterable[FilmType]:
        queryset: List[Film] = Film.objects.all()

        return queryset
