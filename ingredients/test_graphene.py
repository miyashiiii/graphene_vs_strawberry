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
    def test_query(self, client):
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
            "/graphql", data={"query": query}, content_type="application/json"
        )

        assert res.status_code == 200
        result = res.json()
        assert result["data"]["categoryByName"] == {
            "id": str(category.id),
            "name": category.name,
            "ingredients": [{"id": str(ingredient.id), "name": ingredient.name}],
        }
