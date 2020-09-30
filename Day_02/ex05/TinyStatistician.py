import statistics
import numpy as np
from math import sqrt


class TinyStatistician:

    def mean(self, x):
        if not x:
            return None
        res = float(0)
        for e in x:
            res += e
        return float(res / len(x))

    def median(self, x):
        if not x:
            return None
        x.sort()
        ln = len(x)
        if ln % 2:
            return float(x[int(ln / 2)])
        else:
            i = int(ln / 2)
            return self.mean([x[i], x[i - 1]])

    def quartile(self, x, percentile):
        if percentile not in [25, 75] or not x:
            return None
        x.sort()
        ln = len(x)
        lln = ln
        if percentile == 75:
            lln *= 3
        if ln % 4:
            return float(x[lln // 4])
        else:
            return float(x[(lln // 4) - 1])

    def var(self, x):
        if not x:
            return None
        m = len(x)
        mean = self.mean(x)
        res = 0
        for elem in x:
            res += (elem - mean) ** 2
        return float(res / m)

    def std(self, x):
        return sqrt(self.var(x))


def main():
    t = TinyStatistician()
    a = [1, 42, 300, 10, 59, 53, 58]
    b = [1, 42, 300, 10, 59, 101, 50, 90, 23, 53]
    print(t.mean(a))
    print(t.mean(list()))
    print(t.median(a))
    print(t.median(list()))
    print(t.median(b))
    print(statistics.median(b))
    print("Quartile a")
    print(t.quartile(a, 25))
    print(np.percentile(a, 25, interpolation="lower"))
    print(t.quartile(a, 75))
    print(np.percentile(a, 75, interpolation="lower"))
    print("Quartile b")
    print(t.quartile(b, 25))
    print(np.percentile(b, 25, interpolation="lower"))
    print(t.quartile(b, 75))
    print(np.percentile(b, 75, interpolation="lower"))
    print("Variance")
    print(t.var(a))
    print(np.var(a))
    print(t.var(b))
    print(np.var(b))
    print("STD")
    print(t.std(a))
    print(np.std(a))
    print(t.std(b))
    print(np.std(b))


if __name__ == "__main__":
    main()
