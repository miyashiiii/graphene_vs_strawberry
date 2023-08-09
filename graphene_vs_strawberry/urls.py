from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView as GrapheneGraphQLView
from strawberry.django.views import GraphQLView as StrawberryGraphQLView

from graphene_vs_strawberry.schema_graphene import schema as graphene_schema
from graphene_vs_strawberry.schema_strawberry import schema as strawberry_schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "graphene",
        csrf_exempt(GrapheneGraphQLView.as_view(graphiql=True, schema=graphene_schema)),
    ),
    path("strawberry", StrawberryGraphQLView.as_view(schema=strawberry_schema)),
]
