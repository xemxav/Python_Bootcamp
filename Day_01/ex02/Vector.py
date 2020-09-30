class Vector:
    def __init__(self, values):
        self.values = list()
        if isinstance(values, list):
            for v in values:
                if isinstance(v, float) or isinstance(v, int):
                    self.values.append(float(v))
                else:
                    raise ValueError(
                        "You must instance with a list of floats")
        elif isinstance(values, tuple) and len(values) == 2:
            for v in range(values[0], values[1]):
                self.values.append(float(v))
        elif isinstance(values, int):
            for v in range(0, values):
                self.values.append(float(v))
        else:
            raise ValueError(
                "You must instance with a list of floats")
        self.size = len(self.values)

    def __str__(self):
        return "(Vector {})".format(self.values)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __add__(self, other):
        if isinstance(other, Vector) and other.size == self.size:
            vals = list()
            for i in range(0, self.size):
                vals.append(self.values[i] + other.values[i])
            return Vector(vals)
        elif isinstance(other, int) or isinstance(other, float):
            vals = list()
            for i in range(0, self.size):
                vals.append(self.values[i] + float(other))
            return Vector(vals)
        else:
            raise ValueError(
                "You must add two vector of "
                "the same dimmension or a scalar")

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Vector) and other.size == self.size:
            vals = list()
            for i in range(0, self.size):
                vals.append(self.values[i] - other.values[i])
            return Vector(vals)
        elif isinstance(other, int) or isinstance(other, float):
            vals = list()
            for i in range(0, self.size):
                vals.append(self.values[i] - float(other))
            return Vector(vals)
        else:
            raise ValueError(
                "You must substract two vector "
                "of the same dimmension or a scalar")

    def __rsub__(self, other):
        if isinstance(other, Vector) and other.size == self.size:
            vals = list()
            for i in range(0, self.size):
                vals.append(other.values[i] - self.values[i])
            return Vector(vals)
        elif isinstance(other, int) or isinstance(other, float):
            vals = list()
            for i in range(0, self.size):
                vals.append(float(other) - self.values[i])
            return Vector(vals)
        else:
            raise ValueError("You must add two vector of the same dimmension")

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float) and other != 0:
            return Vector([v / other for v in self.values])
        else:
            raise ValueError("You must use a scalar different of 0")

    def __rtruediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            for v in self.values:
                if v == 0:
                    raise ValueError("Can not divide by 0")
            return Vector([other / v for v in self.values])
        else:
            raise ValueError("You must use a scalar different of 0")

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector([v * other for v in self.values])
        elif isinstance(other, Vector) and other.size == self.size:
            ret = float(0)
            for i in range(0, self.size):
                ret += other.values[i] * self.values[i]
            return ret
        else:
            raise ValueError(
                "You can multiply vector of same dimension or scalar")

    def __rmul__(self, other):
        return self * other
