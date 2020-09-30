from random import randint


def exiting():
    print("Goodbye!")
    quit(0)


def guess(number, try_nb=1):
    inp = input("What's your guess between 1 and 99?\n")
    if inp.isdigit() is True:
        nb = int(inp)
        if nb == number:
            if try_nb == 1:
                if nb != 42:
                    print("Congratulations you won on your first attempt !")
                else:
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
                    print("Congratulations! You got it on your first try!")
            elif try_nb > 1:
                print("Congratulations, you've got it\nYou won in %d attenpts!" % try_nb)
            exit(1)
        elif nb < number:
            print("Too low!")
        elif nb > number:
            print("Too high!")
    elif inp == "exit":
        exiting()
    else:
        print("That's not a number.")
    return guess(number, try_nb + 1)


def main():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.\nGood luck!")
    guess(randint(1, 99))


if __name__ == "__main__":
    main()
