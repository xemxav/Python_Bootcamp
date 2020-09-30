from ex02.Vector import Vector


class Matrix:

    def __init_with_list(self, lst):
        col = 0
        for i, l in enumerate(lst):
            if not isinstance(l, list):
                raise ValueError("must be instanced with "
                                 "list of float for data")
            for y, elem in enumerate(l):
                try:
                    l[y] = float(elem)
                except ValueError:
                    raise NotImplemented("must be number")
            if i == 0:
                col = len(lst)
            elif col != len(lst):
                raise ValueError("must be same number of element in list")
        self.data = lst
        self.shape = (i + 1, col)

    def __init_with_tuple(self, t):
        if len(t) > 2:
            raise ValueError("too much value in tuple")
        self.shape = t
        for row in range(0, t[0]):
            nl = list()
            for elem in range(0, t[1]):
                nl.append(float(0))
            self.data.append(nl)

    def __init__(self, *args):
        self.data = list()
        self.shape = tuple()
        if len(args) == 0:
            raise ValueError("must be initialize with data and/or shape")
        elif len(args) == 1:
            if isinstance(args[0], list):
                self.__init_with_list(args[0])
            elif isinstance(args[0], tuple):
                self.__init_with_tuple(args[0])
        elif len(args) == 2:
            if isinstance(args[0], list):
                self.__init_with_list(args[0])
                if self.shape != args[1]:
                    raise ValueError("Data and shape do not match")
            else:
                raise ValueError("args not in good order")
        else:
            raise ValueError("Too many args")

    def __str__(self):
        return "(Matrix data:{} shape{})".format(self.data, self.shape)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __add__(self, other):
        if isinstance(other, Matrix) and other.shape == self.shape:
            new = Matrix(self.shape)
            for row in range(0, new.shape[0]):
                for col in range(0, new.shape[1]):
                    new.data[row][col] = other.data[row][col] \
                                         + self.data[row][col]
            return new
        else:
            raise NotImplemented("You can only add a Vector "
                                 "or Matrix instance to a Matrix instance")

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Matrix) and other.shape == self.shape:
            new = Matrix(self.shape)
            for row in range(0, new.shape[0]):
                for col in range(0, new.shape[1]):
                    new.data[row][col] = self.data[row][col] \
                                         - other.data[row][col]
            return new
        else:
            raise NotImplemented("You can only add a Vector "
                                 "or Matrix instance to a Matrix instance")

    def __rsub__(self, other):
        if isinstance(other, Matrix) and other.shape == self.shape:
            new = Matrix(self.shape)
            for row in range(0, new.shape[0]):
                for col in range(0, new.shape[1]):
                    new.data[row][col] = other.data[row][col] \
                                         - self.data[row][col]
            return new
        else:
            raise NotImplemented("You can only add a Vector "
                                 "or Matrix instance to a Matrix instance")

    def __mul__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) and other:
            new = Matrix(self.shape)
            for row in range(0, new.shape[0]):
                for col in range(0, new.shape[1]):
                    new.data[row][col] = self.data[row][col] * other
            return new
        if isinstance(other, Vector) and other.size == self.shape[1]:
            new = Vector(self.shape[1])
            for i in range(0, self.shape[1]):
                new.values[i] = 0
                for y in range(0, self.shape[0]):
                    new.values[i] += self.data[i][y] * other.values[y]
            return new
        elif isinstance(other, Matrix) and self.shape[0] == other.shape[1]:
            new = Matrix((self.shape[0], other.shape[1]))
            for i in range(0, self.shape[0]):
                for j in range(0, other.shape[1]):
                    for k in range(0, other.shape[0]):
                        new.data[i][j] += self.data[i][k] * other.data[k][j]
            return new
        raise NotImplemented("You can only add a Vector "
                             "or Matrix instance to a Matrix instance")

    def __rmul__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) and other:
            new = Matrix(self.shape)
            for row in range(0, new.shape[0]):
                for col in range(0, new.shape[1]):
                    new.data[row][col] = self.data[row][col] * other
            return new
        if isinstance(other, Vector) and other.size == self.shape[1]:
            new = Vector(self.shape[1])
            for i in range(0, self.shape[1]):
                new.values[i] = 0
                for y in range(0, self.shape[0]):
                    new.values[i] += self.data[i][y] * other.values[y]
            return new
        elif isinstance(other, Matrix) and self.shape[0] == other.shape[1]:
            new = Matrix((other.shape[0], self.shape[1]))
            for i in range(0, other.shape[0]):
                for j in range(0, self.shape[1]):
                    for k in range(0, self.shape[0]):
                        new.data[i][j] += other.data[i][k] * self.data[k][j]
            return new

    def __truediv__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) and other:
            new = Matrix(self.shape)
            for row in range(0, new.shape[0]):
                for col in range(0, new.shape[1]):
                    new.data[row][col] = self.data[row][col] / other
            return new

        else:
            raise NotImplemented("Only scalars")

    def __rtruediv__(self, other):
        raise NotImplemented("Only scalars")
