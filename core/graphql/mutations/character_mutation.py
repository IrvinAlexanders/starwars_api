import strawberry

from core.models import Character
from core.graphql.types import CharacterType


@strawberry.input
class CreateCharacterInput:
    """Input type for creating a new character.
    """
    name: str = strawberry.field(description="The name of the character.")
    birth_year: str | None = strawberry.field(
        default=None,
        description="The birth year of the character, can be blank or null."
    )
    gender: str | None = strawberry.field(
        default=None,
        description="The gender of the character, can be blank or null."
    )


@strawberry.type
class CharacterMutations:
    """Mutations for creating and updating characters in the Star Wars universe.
    This class contains methods for creating a new character.
    """
    @strawberry.mutation
    def create_character(self, input: CreateCharacterInput) -> CharacterType:
        return Character.objects.create(**input.__dict__)
