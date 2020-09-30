class Recipe:
    recipe_type_ok = ["starter", "lunch", "dessert"]

    def __init__(self, **kwargs):
        self.name = str()
        self.cooking_lvl = int()
        self.ingredients = list()
        self.description = ""
        self.recipe_type = str()
        if 'name' in kwargs.keys() and isinstance(kwargs['name'], str) \
                and len(kwargs['name']) > 0:
            self.name = kwargs['name']
        else:
            raise ValueError("The name must be a string")
        if 'cooking_lvl' in kwargs.keys() \
                and isinstance(kwargs['cooking_lvl'], int) \
                and kwargs['cooking_lvl'] in range(1, 6):
            self.cooking_lvl = kwargs['cooking_lvl']
        else:
            raise ValueError(
                "The cooking_lvl must be an integer between 1 and 5")
        if 'cooking_time' in kwargs.keys() and isinstance(
                kwargs['cooking_time'], int) and kwargs['cooking_time'] >= 0:
            self.cooking_time = kwargs['cooking_time']
        else:
            raise ValueError("The cooking_time must be a positive integer")
        if 'recipe_type' in kwargs.keys() and isinstance(kwargs['recipe_type'],
                                                         str) \
                and kwargs['recipe_type'] in self.recipe_type_ok:
            self.recipe_type = kwargs['recipe_type']
        else:
            raise ValueError("The recipe_type must be a str : "
                             "starter, lunch or dessert")
        if 'ingredients' in kwargs.keys() \
                and isinstance(kwargs['ingredients'], list) \
                and len(kwargs['ingredients']) > 0:
            for ing in kwargs['ingredients']:
                if not isinstance(ing, str):
                    raise ValueError(
                        "The ingredients in the list must be strings")
            self.ingredients = kwargs['ingredients']
        else:
            raise ValueError(
                "You must add a list of ingredients (str only in the list)")
        if 'description' not in kwargs.keys():
            pass
        elif isinstance(kwargs['description'], str):
            self.description = kwargs['description']
        else:
            raise ValueError("The description must be a string")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "The name of the recipe is %s\n" % self.name
        txt += "It is best serve for %s\n" % self.recipe_type
        txt += f"It takes {self.cooking_time} minutes to cook a" \
               f"nd the cooking level is {self.cooking_lvl}\n"
        txt += "The ingredients are:\n"
        for i in self.ingredients:
            txt += "\t- " + i + "\n"
        if len(self.description) > 0:
            txt += self.description
        txt += "\r"
        return txt
