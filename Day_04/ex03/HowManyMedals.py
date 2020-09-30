from ex01.FileLoader import FileLoader


def howmanymedals(df, name):
    if name not in df.Name.values:
        return "Not a good name"
    res = dict()
    df = df[df.Name == name].sort_values("Year")
    for year in df.Year.values:
        year_dict = dict()
        for m in ['Gold', 'Silver', "Bronze"]:
            year_dict[m[0]] = df[(df.Medal == m) & (df.Year == year)].shape[0]
        res[year] = year_dict
    return res


def main():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    p = howmanymedals(data, 'Kjetil Andr Aamodt')
    print(p)


if __name__ == "__main__":
    main()
