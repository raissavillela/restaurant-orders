import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self._load_data(source_path)

    def _load_data(self, source_path: str) -> None:
        with open(source_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dish_name = row['dish']
                price = float(row['price'])
                ingredient_name = row['ingredient']
                recipe_amount = int(row['recipe_amount'])

                ingredient = Ingredient(ingredient_name)

                dish = next((d for d in self.dishes if d.name == dish_name),
                            None)
                if dish is None:
                    dish = Dish(dish_name, price)
                    self.dishes.add(dish)

                dish.add_ingredient_dependency(ingredient, recipe_amount)
