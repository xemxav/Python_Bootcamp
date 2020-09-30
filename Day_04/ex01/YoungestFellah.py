from .FileLoader import FileLoader


def youngestFellah(data, year):
    youngest = {
        "F": None,
        "M": None,
    }
    if year not in data.Year.values:
        print("Not an olympic year")
        return None
    for key in youngest.keys():
        df = data[(data.Sex == key) & (data.Year == year)]
        youngest[key] = df.Age.min()
    return youngest


def main():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    d = youngestFellah(data, 1936)
    print(d)


if __name__ == "__main__":
    main()
