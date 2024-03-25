from src.models.dish import Dish  # noqa: F401, E261, E501
from tests.dishes import DISHES
from tests.ingredients import INGREDIENTS
from src.models.ingredient import Restriction
import pytest


# Req 2
def test_dish():
    dish_mock = DISHES[0]
    dish = Dish(dish_mock.name, dish_mock.price)

    assert dish.name == dish_mock.name

    repr_response = f"Dish('{dish_mock.name}', R${dish_mock.price:.2f})"

    assert dish.__repr__() == repr_response
    assert dish.__hash__() == dish.__hash__()
    assert dish == dish

    another_dish_mock = DISHES[1]
    another_dish = Dish(another_dish_mock.name, another_dish_mock.price)

    assert dish.__hash__() != another_dish.__hash__()
    assert dish != another_dish

    with pytest.raises(TypeError):
        Dish(dish_mock.name, "1")

    with pytest.raises(ValueError):
        Dish(dish_mock.name, -1)

    dish.add_ingredient_dependency(INGREDIENTS[0], 100)
    assert dish.get_ingredients() == {INGREDIENTS[0]}
    assert dish.get_restrictions() == {
        Restriction.ANIMAL_DERIVED, Restriction.LACTOSE
    }
