import strawberry

from core.models import Planet


@strawberry.django.type(Planet)
class PlanetType:
    """Represents a planet in the Star Wars universe.

    Attributes:
        id (ID): The unique identifier of the planet.
        name (str): The name of the planet.
        climate (str | None): The climate of the planet, can be blank or null.
        terrain (str | None): The terrain of the planet, can be blank or null.
        population (str | None): The population of the planet, can be blank or null.
    """

    id: strawberry.ID
    name: str
    climate: str | None
    terrain: str | None
    population: str | None