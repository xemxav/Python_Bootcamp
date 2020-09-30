import pandas as pd


class FileLoader:

    def load(self, path):
        new = pd.read_csv(path, sep=',')
        print("Loading data of dimensions %d x %d" %
              (new.shape[0], new.shape[1]))
        return new

    def display(self, df, n):
        if (n >= 0):
            print(df.head(n))

        else:
            print(df.tail(-n))
        print("\n[%d rows x %d colums]" % (n, df.shape[1]))

