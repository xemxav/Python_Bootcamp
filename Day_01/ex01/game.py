class GotChracter:

    def __init__(self, first_name=None, is_alive=True):
        self.is_alive = is_alive
        self.first_name = first_name


class Targaryen(GotChracter):
    """A class representing the true rulers of Westeros"""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=True)
        self.family_name = "Targaryen"
        self.house_words = "Fire and blood"
        self.is_alive = is_alive

    def print_house_word(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


def main():
    pass


if __name__ == "__main__":
    main()
