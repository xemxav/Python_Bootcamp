import numpy as np


class NumPyCreator:
    def from_list(self, lst):
        return np.array(lst)

    def from_tuple(self, tpl):
        return np.array(tpl)

    def from_iterable(self, itr):
        return np.array(itr)

    def from_shape(self, shape, value=0):
        return np.full(shape, value)

    def random(self, shape):
        return np.random.rand(shape[0], shape[1])

    def identity(self, n):
        return np.identity(n)


def main():
    npc = NumPyCreator()
    print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
    print(npc.from_tuple(("a", "b", "c")))
    print(npc.from_iterable(range(5)))
    shape = (3, 5)
    print(npc.from_shape(shape))
    print(npc.random(shape))
    print(npc.identity(4))


if __name__ == "__main__":
    main()
