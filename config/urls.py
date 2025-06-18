from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # GraphQL API
    path("graphql/", include("core.urls")),
]