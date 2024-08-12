import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction


def test_dish():
    dish = Dish("Lasanha", 25.90)
    assert isinstance(dish, Dish)
    assert dish.name == "Lasanha"
    assert dish.price == 25.90

    assert repr(dish) == "Dish('Lasanha', R$25.90)"

    same_dish = Dish("Lasanha", 25.90)
    different_dish = Dish("Ravioli", 18.50)
    assert dish == same_dish
    assert dish != different_dish

    assert hash(dish) == hash(same_dish)
    assert hash(dish) != hash(different_dish)

    ingredient1 = Ingredient("queijo parmesão")
    ingredient2 = Ingredient("presunto")
    dish.add_ingredient_dependency(ingredient1, 150)
    dish.add_ingredient_dependency(ingredient2, 50)
    assert dish.recipe.get(ingredient1) == 150
    assert dish.recipe.get(ingredient2) == 50

    expected_restrictions = {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,

    }
    assert dish.get_restrictions() == expected_restrictions

    expected_ingredients = {ingredient1, ingredient2}
    assert dish.get_ingredients() == expected_ingredients

    with pytest.raises(TypeError):
        Dish("Invalid Dish", "not a float")

    with pytest.raises(ValueError):
        Dish("Invalid Dish", -5.00)
