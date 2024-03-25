from models.ingredient import Ingredient
from models.dish import Dish
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = self.dishes_list()

    def dishes_list(self):
        with open(self.source_path, newline='') as file:
            file_reader = csv.DictReader(file)
            dishes = set()

            for line in file_reader:
                dish = Dish(line['dish'], float(line['price']))
                ingredient = Ingredient(line['ingredient'])

                if dish not in dishes:
                    dish.add_ingredient_dependency(
                        ingredient, int(line['recipe_amount'])
                    )

                else:
                    for existent_dish in dishes:
                        if existent_dish == dish:
                            existent_dish.add_ingredient_dependency(
                                ingredient, int(line['recipe_amount'])
                            )

                dishes.add(dish)

        return dishes
