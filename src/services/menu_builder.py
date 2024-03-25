from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        main_menu = list()
        filtered_dishes = set()

        if not restriction:
            filtered_dishes = self.menu_data.dishes

        else:
            for existent_dish in self.menu_data.dishes:
                recipe_restrictions = existent_dish.get_restrictions()
                if restriction not in recipe_restrictions:
                  filtered_dishes.add(existent_dish)

        for dish in filtered_dishes:
            dish_dict = {
                "dish_name": dish.name,
                "ingredients": dish.recipe,
                "price": dish.price,
                "restrictions": dish.get_restrictions()
            }

            main_menu.append(dish_dict)

        return main_menu
