from src.models.ingredient import Ingredient, Restriction


def test_ingredient():

    ingredient = Ingredient("creme de leite")
    assert isinstance(ingredient, Ingredient)
    assert ingredient.name == "creme de leite"

    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingredient.restrictions == expected_restrictions

    assert repr(ingredient) == "Ingredient('creme de leite')"

    same_ingredient = Ingredient("creme de leite")
    different_ingredient = Ingredient("carne")
    assert ingredient == same_ingredient
    assert ingredient != different_ingredient

    assert hash(ingredient) == hash(same_ingredient)
    assert hash(ingredient) != hash(different_ingredient)
