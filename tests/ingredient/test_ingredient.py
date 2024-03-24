from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from tests.ingredients import INGREDIENTS


# Req 1
def test_ingredient():
    ingredient_mock = INGREDIENTS[0]
    ingredient = Ingredient(ingredient_mock.name)

    # falha caso o atributo name de um ingrediente seja diferente que o passado ao construtor
    assert ingredient.name == ingredient_mock.name

    # falha caso o atributo restrictions de um ingrediente não contenha os valores corretos para o alimento passado
    assert ingredient.restrictions == ingredient_mock.restrictions

    #  falha caso a implementação do método __repr__ retorne um valor inadequado
    assert ingredient.__repr__() == f"Ingredient('{ingredient_mock.name}')"

    # falha caso a classe retorne hashes diferentes para dois ingredientes iguais
    assert ingredient.__hash__() == ingredient.__hash__()

    # falha caso a comparação de igualdade de dois ingredientes iguais (ou de um ingrediente com ele mesmo) seja falsa
    assert ingredient == ingredient

    another_ingredient_mock = INGREDIENTS[1]
    another_ingredient = Ingredient(another_ingredient_mock.name)

    # falha caso a classe retorne hashes iguais para dois ingredientes diferentes
    assert ingredient.__hash__() != another_ingredient.__hash__()

    # falha caso a comparação de igualdade de dois ingredientes diferentes seja verdadeira
    assert ingredient != another_ingredient
