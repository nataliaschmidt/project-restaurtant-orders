from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    INGREDIENT_1 = Ingredient("ovo")
    INGREDIENT_2 = Ingredient("bacon")

    DISH_1 = Dish("Omelete", 10)
    DISH_2 = Dish("Omelete", 10)
    DISH_3 = Dish("Omelete", 2)

    DISH_1.add_ingredient_dependency(INGREDIENT_1, 2)
    DISH_1.add_ingredient_dependency(INGREDIENT_2, 1)
    # print(DISH_1.get_restrictions())

    assert DISH_1.name == "Omelete"
    assert DISH_1.price == 10

    """Testes dos casos de erro no price"""
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Omelete", -10)

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Omelete", "10")

    """Teste para o método __repr__"""
    assert DISH_1.__repr__() == "Dish('Omelete', R$10.00)"

    """Teste para o método __eq__"""
    assert DISH_1.__eq__(DISH_2) is True
    assert DISH_1.__eq__(DISH_3) is False

    """Teste para o método __hash__"""
    assert DISH_1.__hash__() == DISH_2.__hash__()
    assert DISH_1.__hash__() != DISH_3.__hash__()

    """Teste para os métodos add_ingredient_dependency e get_get_ingredients"""
    DISH_1.add_ingredient_dependency(INGREDIENT_1, 2)
    assert DISH_1.get_ingredients() == {Ingredient("ovo"), Ingredient("bacon")}

    """Teste para o método get_restrictions"""
    assert Restriction.ANIMAL_DERIVED in DISH_1.get_restrictions()
    assert Restriction.ANIMAL_MEAT in DISH_1.get_restrictions()
