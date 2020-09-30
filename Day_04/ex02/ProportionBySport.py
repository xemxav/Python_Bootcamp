from ex01.FileLoader import FileLoader


def proportionBySport(df, year, sport, gender):
    df = df[(df.Year == year) & (df.Sex == gender)]
    df = df.drop_duplicates(subset="Name")
    total = df.shape[0]
    part = df[df.Sport == sport].shape[0]
    return part / total


def main():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    p = proportionBySport(data, 2004, 'Tennis', 'F')
    print(p)


if __name__ == "__main__":
    main()
