from django.test import Client
import pytest
from core.graphql import schema
from core.tests.base import SWAPITestCase, SWAPIGraphQLTestCase
from core.graphql.types import CharacterType, FilmType, PlanetType
from core.models import Film, Planet, Character

from strawberry.django.test import GraphQLTestClient


@pytest.fixture
def gql_client():
    client = Client()
    return GraphQLTestClient(client=client)

@pytest.mark.django_db
def test_character_type_query(gql_client):
    # Arrange
    planet = Planet.objects.create(
        name="Tatooine",
        climate="arid",
        terrain="desert",
        population=200000
    )

    film = Film.objects.create(
        title="A New Hope",
        episode_id=4,
        opening_crawl="It is a period of civil war...",
        director="George Lucas",
        producers="Gary Kurtz",
        release_date="1977-05-25"
    )

    film.planets.add(planet)

    character = Character.objects.create(
        name="Luke Skywalker",
        birth_year="19BBY",
        gender="Male"
    )
    character.films.add(film)

    # Act
    response = gql_client.query(
        """
        query {
            characters {
                edges {
                    node {
                        name
                        birthYear
                        gender
                        films {
                            title
                            planets {
                                name
                            }
                        }
                    }
                }
            }
        }
        """
    )

    node = response.data["characters"]["edges"][0]["node"]

    # Assert
    assert node["name"] == "Luke Skywalker"
    assert node["birthYear"] == "19BBY"
    assert node["gender"] == "Male"
    assert node["films"][0]["title"] == "A New Hope"
    assert len(node["films"][0]["planets"]) == 1

@pytest.mark.django_db
def test_character_with_films(gql_client):
    # Arrange
    film = Film.objects.create(
        title="A New Hope",
        episode_id=4,
        opening_crawl="It is a period of civil war...",
        director="George Lucas",
        producers="Gary Kurtz",
        release_date="1977-05-25"
    )

    character = Character.objects.create(
        name="Luke Skywalker",
        birth_year="19BBY",
        gender="male"
    )
    character.films.add(film)

    # Act
    response = gql_client.query(
        """
        query {
            characters {
                edges {
                    node {
                        name
                        films {
                            title
                            openingCrawl
                            director
                        }
                    }
                }
            }
        }
        """
    )

    node = response.data["characters"]["edges"][0]["node"]

    # Assert
    assert node["name"] == "Luke Skywalker"
    assert node["films"][0]["title"] == "A New Hope"
    assert node["films"][0]["director"] == "George Lucas"
