import pandas as pd
from ex06.MyPlotLib import MyPlotLib
from ex00.FileLoader import FileLoader
from matplotlib import pyplot as plt


class Komparator:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            print("Not a DataFrame")
            exit(1)
        self.df = df
        self.mp = MyPlotLib()

    def compare_box_plots(self, categorical_var, numerical_var):
        for c in self.df[categorical_var].unique():
            df = self.df[self.df[categorical_var] == c]
            df.boxplot(column=numerical_var)
            plt.title(c)
            plt.show()

    def density(self, categorical_var, numerical_var):
        for c in self.df[categorical_var].unique():
            df = self.df[self.df[categorical_var] == c]
            df[numerical_var].plot.density()
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        for c in self.df[categorical_var].unique():
            df = self.df[self.df[categorical_var] == c]
            df[numerical_var].hist()
        plt.show()


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    k = Komparator(data)
    k.compare_histograms("Sex", "Height")
