import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_dish():

    dish1 = Dish("Spaghetti Carbonara", 12.99)

    assert dish1.name == "Spaghetti Carbonara"
    assert dish1.name != "Spaghetti"
    assert dish1.price == 12.99
    ingredientes = Ingredient('manteiga')
    dish1.add_ingredient_dependency(ingredientes, 10)
    assert ingredientes in dish1.recipe
    assert dish1.recipe[ingredientes] == 10
    restricoes = dish1.get_restrictions()
    assert Restriction.LACTOSE in restricoes
    assert Restriction.ANIMAL_DERIVED in restricoes

    dish2 = Dish("Sushi", 10.99)
    ingredientes2 = Ingredient('salmão')
    dish2.add_ingredient_dependency(ingredientes2, 10)
    assert repr(dish2) == "Dish('Sushi', R$10.99)"

    ingredientes_get = dish2.get_ingredients()
    assert ingredientes2 in ingredientes_get

    dish5 = Dish("Spaghetti Carbonara", 12.99)
    dish3 = Dish("Lasagna", 10.99)

    assert dish1 == dish5
    assert dish1 != dish3

    assert hash(dish1) == hash(dish5)
    assert hash(dish1) != hash(dish3)

    with pytest.raises(
            ValueError):
        Dish("Invalid Dish", 0)
