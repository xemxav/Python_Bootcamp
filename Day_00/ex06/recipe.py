cookbook = {
    'sandwich': {
        'ingredients': ["ham", "bread", "cheese", "tomatoes"],
        'meal': "lunch",
        'prep_time': 10,
    },
    'cake': {
        'ingredients': ["flour", "sugar", "eggs"],
        'meal': "dessert",
        'prep_time': 60,
    },
    'salad': {
        'ingredients': ["avocado", "arugula", "tomatoes", "spinach"],
        'meal': "lunch",
        'prep_time': 15,
    },
}


def add_recipe():
    name = input("Please enter a name for the recipe: ")
    meal = input("What is the proper meal for this recipe? ")
    ing = input("Please enter each ingredient separated by a comma: ")
    prep = input("Please enter the preptime in minute:")
    if not prep.isdigit():
        print("The information are incorrect")
        return
    ing = ing.split(',')
    ing = [i.strip() for i in ing]
    cookbook[name] = {
        'ingredients': ing,
        'meal': meal,
        'prep_time': int(prep),
    }
    print("\nHere is the recorded recipe:")
    print_recipe(name)


def delete_recipe():
    r = input("Please enter the recipe's name to delete it:")
    try:
        del cookbook[r]
        print("The recipe for %s has been deleted" % r)
    except KeyError:
        print("This recipe is not in the cookbook")


def print_recipe(r):
    print("Recipe for %s:" % r)
    print("Ingredients list:", cookbook[r]['ingredients'])
    print("To be eaten for %s." % cookbook[r]['meal'])
    print("Takes %d minutes of cooking." % cookbook[r]['prep_time'])
    print('\n', end='')


def sel_recipe():
    r = input("Please enter the recipe's name to get its details:")
    if r in cookbook.keys():
        print_recipe(r)
    else:
        print("This recipe is not in the cookbook")


def print_cookbook():
    for r in cookbook.keys():
        print_recipe(r)


def quitting():
    print("Cookbook closed")
    quit(0)


instruction = {
    1: add_recipe,
    2: delete_recipe,
    3: sel_recipe,
    4: print_cookbook,
    5: quitting,
}


def get_user_instruction():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    i = input()
    if not i.isdigit() or int(i) < 0 or int(i) > 5:
        print("This option does not exist, please type the corresponding number.")
        print("To exit, enter 5.")
        return get_user_instruction()
    else:
        return int(i)


def main():
    while 1:
        ins = get_user_instruction()
        instruction[ins]()


if __name__ == '__main__':
    main()
