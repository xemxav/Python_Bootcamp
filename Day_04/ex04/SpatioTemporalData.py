from ex01.FileLoader import FileLoader
import pandas as pd


class SpatioTemporalData:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise NotImplemented
        self.df = df.sort_values("Games").drop_duplicates(subset="Games")

    def when(self, location):
        if location not in self.df.City.values:
            return "Not an olympic city"
        df = self.df[self.df.City == location]
        return list(df.Year.values)

    def where(self, year):
        if year not in self.df.Year.values:
            return "Not an olympic year"
        df = self.df[self.df.Year == year]
        return list(df.City.values)


def main():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    print(sp.when("Athina"))
    print(sp.when("Paris"))
    print(sp.when("Lyon"))
    print(sp.where(2100))
    print(sp.where(1996))


if __name__ == "__main__":
    main()
