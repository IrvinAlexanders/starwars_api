from django.test import TestCase
from strawberry.django.test import GraphQLTestClient


class SWAPITestCase(TestCase):
    """Base test case for the Star Wars API application.

    This class provides common setup and teardown methods for tests.
    It can be extended by other test cases to share common functionality.
    """
    ...


class SWAPIGraphQLTestCase(GraphQLTestClient):
    """Base test case for GraphQL tests in the Star Wars API application.

    This class provides a GraphQL client for testing GraphQL queries and mutations.
    It can be extended by other test cases that require GraphQL functionality.
    """
    ...