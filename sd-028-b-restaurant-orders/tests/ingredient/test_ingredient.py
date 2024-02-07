from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_ingredient():
    ing1 = Ingredient('tomate')
    assert ing1.name == 'tomate'

    ing2 = Ingredient('queijo mussarela')
    assert ing2.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
        }
    ing3 = Ingredient('presunto')

    assert ing2 != ing3

    ing4 = Ingredient('cenoura')
    ing5 = Ingredient('cebola')
    ing6 = Ingredient('tomate')

    assert ing4 != ing5
    assert ing1 == ing6

    assert repr(ing1) == "Ingredient('tomate')"
    assert repr(ing2) == "Ingredient('queijo mussarela')"

    assert hash(ing1) == hash(ing6)

    assert hash(ing1) != hash(ing2)
