"""Kochbuch-App"""
import json


def adjust_recipe(my_recipe, my_num_people):
    factor = my_num_people / my_recipe["servings"]
    adjusted_ingredients = {ingredient: int(quantity * factor) for ingredient, quantity in my_recipe["ingredients"]
    .items()}
    return {
        "title": my_recipe["title"],
        "ingredients": adjusted_ingredients,
        "servings": my_num_people
    }


def load_recipe(my_json_string):
    return json.loads(my_json_string)


if __name__ == "__main__":
    recipe_json = '{"title": "Spaghetti Bolognese", ' \
                  '"ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}"'
    recipe = load_recipe(recipe_json)
    print(recipe)
    adjusted_recipe = adjust_recipe(recipe, 2)
    print(adjusted_recipe)
