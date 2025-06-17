import strawberry

from core.models import Planet
from core.graphql.types import PlanetType


@strawberry.input
class CreatePlanetInput:
    """Input type for creating a new planet.
    """
    name: str = strawberry.field(description="The name of the planet.")
    climate: str | None = strawberry.field(
        default=None,
        description="The climate of the planet, can be blank or null."
    )
    population: int | None = strawberry.field(
        default=None,
        description="The population of the planet, can be blank or null."
    )


@strawberry.type
class PlanetMutations:
    """Mutations for creating and updating planets in the Star Wars universe.
    This class contains methods for creating a new planet.
    """
    @strawberry.mutation
    def create_planet(self, input: CreatePlanetInput) -> PlanetType:
        return Planet.objects.create(**input.__dict__)
