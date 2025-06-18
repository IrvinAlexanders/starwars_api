import pytest
from strawberry.django.test import GraphQLTestClient
from django.test import Client

from core.models import Character, Planet


@pytest.fixture
def gql_client():
    client = Client()
    return GraphQLTestClient(client=client)

@pytest.mark.django_db
def test_create_character_mutation(gql_client):
    # Arrange
    response = gql_client.query(
        """
        mutation CreateCharacter($input: CreateCharacterInput!) {
            createCharacter(input: $input) {
                id
                name
                birthYear
                gender
            }
        }
        """,
        variables={
            "input": {
                "name": "Leia Organa",
                "birthYear": "19BBY",
                "gender": "female"
            }
        }
    )

    # Act
    data = response.data["createCharacter"]

    # Assert
    assert data["name"] == "Leia Organa"
    assert data["birthYear"] == "19BBY"
    assert data["gender"] == "female"

@pytest.mark.django_db
def test_create_planet_mutation(gql_client):
    # Arrange
    response = gql_client.query(
        """
        mutation CreatePlanet($input: CreatePlanetInput!) {
            createPlanet(input: $input) {
                id
                name
                climate
                population
            }
        }
        """,
        variables={
            "input": {
                "name": "Naboo",
                "climate": "temperate",
                "population": 4500000
            }
        }
    )

    # Act
    data = response.data["createPlanet"]

    # Assert
    assert data["name"] == "Naboo"
    assert data["climate"] == "temperate"
    assert data["population"] == "4500000"

@pytest.mark.django_db
def test_create_film_mutation(gql_client):
    # Arrange
    character = Character.objects.create(name="Han Solo")
    planet = Planet.objects.create(name="Endor", climate="temperate", population=30000)

    response = gql_client.query(
        """
        mutation CreateFilm($input: CreateFilmInput!) {
            createFilm(input: $input) {
                id
                title
                episodeId
                openingCrawl
                director
                producers
                releaseDate
                planets {
                    name
                }
            }
        }
        """,
        variables={
            "input": {
                "title": "Return of the Jedi",
                "episodeId": 6,
                "openingCrawl": "Luke Skywalker has returned to his home planet of Tatooine...",
                "director": "Richard Marquand",
                "producers": "Howard Kazanjian",
                "releaseDate": "1983-05-25",
                "characterIds": [character.id],
                "planetIds": [planet.id]
            }
        }
    )

    # Act
    film = response.data["createFilm"]

    # Assert
    assert film["title"] == "Return of the Jedi"
    assert film["episodeId"] == 6
    assert film["director"] == "Richard Marquand"
    assert film["planets"][0]["name"] == "Endor"