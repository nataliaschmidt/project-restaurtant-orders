# Req 3
import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.__read__(source_path)

    def __read__(self, source_path: str):
        try:
            with open(source_path) as file:
                csv_file = csv.DictReader(file)
                data = [dish for dish in csv_file]
                return self.__dishes__(data)
        except FileNotFoundError:
            print("Path not found")

    def __dishes__(self, data):
        dishes_list = set()

        for row in data:
            for dish in dishes_list:
                if dish.name == row["dish"]:
                    break
            else:
                dish = Dish(row["dish"], float(row["price"]))
                dishes_list.add(dish)

            dish.add_ingredient_dependency(
                Ingredient(row["ingredient"]), float(row["recipe_amount"])
            )
        return dishes_list


# new_dishes = MenuData("tests/mocks/menu_base_data.csv")
# print(new_dishes.dishes)
