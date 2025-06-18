import strawberry

from core.graphql.queries.character_queries import CharacterQueries
from core.graphql.queries.film_queries import FilmQueries
from core.graphql.queries.planet_queries import PlanetQueries
from core.graphql.mutations import CharacterMutations, FilmMutations, PlanetMutations


@strawberry.type
class Query(
    CharacterQueries,
    FilmQueries,
    PlanetQueries,
):
    """Root query type for the Star Wars GraphQL API.
    This class aggregates all the query types for characters, films, and planets.
    """
    pass


@strawberry.type
class Mutation(
    CharacterMutations,
    FilmMutations,
    PlanetMutations,
):
    """Root mutation type for the Star Wars GraphQL API.
    This class aggregates all the mutation types for creating and updating characters,
    films, and planets.
    """
    pass


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)
