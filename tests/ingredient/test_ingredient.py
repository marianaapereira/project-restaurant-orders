from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from tests.ingredients import INGREDIENTS


# Req 1
def test_ingredient():
    ingredient_mock = INGREDIENTS[0]
    ingredient = Ingredient(ingredient_mock.name)

    assert ingredient.name == ingredient_mock.name
    assert ingredient.restrictions == ingredient_mock.restrictions
    assert ingredient.__repr__() == f"Ingredient('{ingredient_mock.name}')"
    assert ingredient.__hash__() == ingredient.__hash__()
    assert ingredient == ingredient

    another_ingredient_mock = INGREDIENTS[1]
    another_ingredient = Ingredient(another_ingredient_mock.name)

    assert ingredient.__hash__() != another_ingredient.__hash__()
    assert ingredient != another_ingredient
