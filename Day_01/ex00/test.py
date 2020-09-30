from ex00.recipe import Recipe
from ex00.book import Book


def main():
    print("Create Cookbook")
    try:
        cookbook = Book(name="My cookbook")
    except ValueError as e:
        print(e)
    try:
        tourte = Recipe(name="tourte", cooking_lvl=5, cooking_time=45,
                        description="une bonne tourte",
                        ingredients=["pate", "viande", ], recipe_type="lunch")
        print(tourte.__str__())
    except ValueError as e:
        print(e)
        exit(1)
    try:
        print("cookbook last_update =", cookbook.last_update)
        cookbook.add_recipe(tourte)
        print("cookbook last_update =", cookbook.last_update)
    except ValueError as e:
        print(e)
    try:
        cake = Recipe(name="cake", cooking_lvl=2, cooking_time=30,
                      description="une bon gateau dans le four",
                      ingredients=["sucre", "farine", "oeuf"],
                      recipe_type="dessert")
    except ValueError as e:
        print(e)
        exit(1)
    try:
        salad = Recipe(name="salad", cooking_lvl=2, cooking_time=30,
                       description="une bon gateau dans le four",
                       ingredients=["sucre", "farine", "oeuf"],
                       recipe_type="starter")
    except ValueError as e:
        print(e)
        exit(1)
    try:
        print("cookbook last_update =", cookbook.last_update)
        cookbook.add_recipe(cake)
        print("cookbook last_update =", cookbook.last_update)
    except ValueError as e:
        print(e)
        exit(1)
    try:
        print("cookbook last_update =", cookbook.last_update)
        cookbook.add_recipe(salad)
        print("cookbook last_update =", cookbook.last_update)
    except ValueError as e:
        print(e)
        exit(1)
    try:
        cookbook.get_recipe_by_name("salad")
    except ValueError as e:
        print(e)
        exit(1)
    try:
        cookbook.get_recipes_by_types("lunch")
    except ValueError as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
