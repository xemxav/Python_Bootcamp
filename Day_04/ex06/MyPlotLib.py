import pandas as pd
from matplotlib import pyplot as plt
from ex00.FileLoader import FileLoader


class MyPlotLib:

    def histogram(self, data, features):
        cols = data.columns
        for f in features:
            if (f not in cols):
                print("%s is not present in the data" % f)
            else:
                data[f].hist()
                plt.title(f)
                plt.show()

    def density(self, data, features):
        cols = data.columns
        for f in features:
            if f not in cols:
                print("%s is not present in the data" % f)
            else:
                data[f].plot.density()
        plt.legend()
        plt.show()

    def pair_plot(self, data, features):
        pd.plotting.scatter_matrix(data[features], diagonal='hist')
        plt.show()

    def box_plot(self, data, features):
        data.boxplot(column=features)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    mp = MyPlotLib()
    features = ['Weight', "Height"]
    mp.histogram(data, features)
    mp.density(data, features)
    mp.pair_plot(data, features)
    mp.box_plot(data, features)
