import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, csv_file_path: str):
        self.csv_file_path = csv_file_path
        self.dishes = self.load_menu()

    def load_menu(self):
        dishes_dict = {}

        with open(self.csv_file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Pula a primeira linha do cabeçalho (caso exista)

            for row in reader:
                dish, price, ingredient, quantity = row
                dish_full = dishes_dict.setdefault(
                    dish, Dish(dish, float(price))
                    )
                ingr = Ingredient(ingredient)
                dish_full.add_ingredient_dependency(ingr, int(quantity))

        return set(dishes_dict.values())
