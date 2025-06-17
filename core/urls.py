from strawberry.django.views import GraphQLView
from django.urls import path

from core.graphql.schema import schema


urlpatterns = [
    path(
        "", GraphQLView.as_view(
            graphiql=True, schema=schema
            )
        ),
]