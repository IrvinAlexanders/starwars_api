import strawberry
from strawberry.relay import Connection
from typing import List

from core.models import Planet
from core.graphql.types import PlanetType


@strawberry.type
class PlanetQueries:
    """Queries for retrieving planets from the Star Wars universe.
    """
    @strawberry.django.field
    def planets(self) -> Connection[PlanetType]:
        return Connection.from_queryset(Planet.objects.all())
