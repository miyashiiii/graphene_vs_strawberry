import pytest

import factory


class CategoryFactory(factory.django.DjangoModelFactory):
    name = "Dairy"

    class Meta:
        model = "ingredients.Category"


class IngredientFactory(factory.django.DjangoModelFactory):
    name = "Eggs"

    class Meta:
        model = "ingredients.Ingredient"


@pytest.mark.django_db
class TestGraphene:
    @pytest.fixture(scope="class")
    def graphene_endpoint(self):
        return "/graphene"

    @pytest.fixture(scope="class")
    def strawberry_endpoint(self):
        return "/strawberry"

    def test_graphene(self, client, graphene_endpoint):
        category = CategoryFactory()
        ingredient = IngredientFactory(category=category)
        query = """
            query {
                categoryByName(name: "Dairy") {
                    id
                    name
                    ingredients {
                    id
                    name
                    }
                }
            }
            """

        res = client.post(
            graphene_endpoint, data={"query": query}, content_type="application/json"
        )

        assert res.status_code == 200
        result = res.json()
        assert result["data"]["categoryByName"] == {
            "id": str(category.id),
            "name": category.name,
            "ingredients": [{"id": str(ingredient.id), "name": ingredient.name}],
        }

    def test_strawberry(self, client, strawberry_endpoint):
        category = CategoryFactory()
        ingredient = IngredientFactory(category=category)
        query = """
            query {
                categoryByName(name: "Dairy") {
                    id
                    name
                    ingredients {
                    id
                    name
                    }
                }
            }
            """

        res = client.post(
            strawberry_endpoint, data={"query": query}, content_type="application/json"
        )

        assert res.status_code == 200
        result = res.json()
        assert result["data"]["categoryByName"] == {
            "id": str(category.id),
            "name": category.name,
            "ingredients": [{"id": str(ingredient.id), "name": ingredient.name}],
        }
