import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = self.read()

    def read(self):
        dishes = set()

        with open(self.source_path, newline='') as file:
            reader = csv.DictReader(file)
            data_dishes = {}

            for row in reader:
                dish = row["dish"]
                price = float(row["price"])
                ingredient = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                if dish not in data_dishes:
                    data_dishes[dish] = Dish(dish, price)

                ingredient_name = Ingredient(ingredient)
                data_dishes[dish].add_ingredient_dependency(ingredient_name,
                                                            recipe_amount)

        dishes.update(data_dishes.values())
        return dishes
