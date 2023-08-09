from typing import List
import strawberry
import strawberry_django
from ingredients import models
from strawberry.types import Info
import strawberry.django

@strawberry_django.type(models.Category)
class Category:
    id: strawberry.auto
    name: strawberry.auto
    ingredients: List["Ingredient"]


@strawberry_django.type(models.Ingredient)
class Ingredient:
    id: strawberry.auto
    name: strawberry.auto
    notes: strawberry.auto
    category: "Category"


@strawberry.type
class Query:
    all_categories: list[Category] = strawberry.django.field()

    @strawberry_django.field
    def category_by_name(self, info, name: str) -> Category:
        return models.Category.objects.filter(name=name).first()


schema = strawberry.Schema(query=Query)
