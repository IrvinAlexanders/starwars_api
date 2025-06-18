import strawberry
from strawberry import relay
from typing import List, Iterable

from core.models import Planet
from core.graphql.types import PlanetType


@strawberry.type
class PlanetQueries:
    """Queries for retrieving planets from the Star Wars universe.
    """
    @relay.connection(
        relay.ListConnection[PlanetType],
        description="Retrieve a list of planets from the Star Wars universe."
    )
    def planets(self) -> Iterable[PlanetType]:
        querset: List[Planet] = Planet.objects.all()

        return querset
