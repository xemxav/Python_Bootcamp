from ex01.FileLoader import FileLoader


def howManyMedalsByCountry(df, country):
    if country not in df.Team.values:
        return "country not in the list"
    res = dict()
    df = df[df.Team == country].sort_values("Year")
    for year in df.Year.values:
        year_dict = dict()
        for m in ['Gold', 'Silver', "Bronze"]:
            year_dict[m[0]] = df[(df.Medal == m) & (df.Year == year)].shape[0]
        res[year] = year_dict
    return res


def main():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    p = howManyMedalsByCountry(data, 'France')
    print(p)


if __name__ == "__main__":
    main()
