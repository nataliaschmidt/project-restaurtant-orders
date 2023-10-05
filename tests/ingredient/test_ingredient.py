from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    INGREDIENT_1 = Ingredient("salmão")
    INGREDIENT_2 = Ingredient("salmão")
    INGREDIENT_3 = Ingredient("farinha")
    INGREDIENT_4 = Ingredient("tomate")

    assert INGREDIENT_1.name == "salmão"
    assert INGREDIENT_3.name == "farinha"

    """Testes para o método __repr__"""
    assert INGREDIENT_1.__repr__() == "Ingredient('salmão')"
    assert INGREDIENT_3.__repr__() == "Ingredient('farinha')"

    """Testes para o método __hash__"""
    assert INGREDIENT_1.__hash__() == INGREDIENT_2.__hash__()
    assert INGREDIENT_1.__hash__() != INGREDIENT_3.__hash__()

    """Testes para o método __eq__"""
    assert INGREDIENT_1.__eq__(INGREDIENT_2) is True
    assert INGREDIENT_1.__eq__(INGREDIENT_3) is False

    """Testes para as restrições"""
    assert INGREDIENT_1.restrictions is not None
    assert INGREDIENT_1.restrictions
    assert Restriction.ANIMAL_MEAT in INGREDIENT_1.restrictions
    assert Restriction.SEAFOOD in INGREDIENT_1.restrictions
    assert Restriction.ANIMAL_DERIVED in INGREDIENT_1.restrictions
    assert Restriction.LACTOSE is not INGREDIENT_1.restrictions
    assert INGREDIENT_4.restrictions == set()
