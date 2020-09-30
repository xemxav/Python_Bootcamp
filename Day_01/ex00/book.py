from datetime import datetime
from ex00.recipe import Recipe


class Book:
    def __init__(self, **kwargs):
        self.recipes_list = {
            'starter': list(),
            'lunch': list(),
            'dessert': list(),
        }
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        if 'name' in kwargs.keys() and isinstance(kwargs['name'], str):
            self.name = kwargs['name']
        else:
            raise ValueError("You must include a name as str")
        print("A book has been create, its name is %s" % self.name)

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for t in self.recipes_list.keys():
            for r in self.recipes_list[t]:
                if r.name == name:
                    print(r.__str__())
                    return
        print("No recipe with the name %s" % name)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in self.recipes_list.keys():
            for r in self.recipes_list[recipe_type]:
                print(r.__str__())
        else:
            raise ValueError("this recipe_type doesn't exist")

    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe):
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
            print(
                f"The recipe {recipe.name} "
                f"has been added to {recipe.recipe_type}")
        else:
            raise ValueError("You did not add a recipe instance")
