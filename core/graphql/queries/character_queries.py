import strawberry
from strawberry import relay
from typing import Iterable

from core.models import Character
from core.graphql.types import CharacterType
from core.utils import constants


@strawberry.type
class CharacterQueries:
    """Queries for retrieving characters from the Star Wars universe.
    """
    @relay.connection(
        relay.ListConnection[CharacterType], 
        description=constants.CHARACTER_QUERY_DESCRIPTION
    )
    def characters(self, name: str | None = None) -> Iterable[CharacterType]:
        """Retrieve a list of characters, optionally filtered by name.
        If no name is provided, all characters are returned.
        """
        queryset = Character.objects.all()
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
