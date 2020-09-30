import pytest
from ex02.Vector import Vector


def test_vector_instanciation():
    vlist = Vector([0.0, 1.0, 2.0])
    print(vlist)
    assert isinstance(vlist, Vector), "Did not create with list"
    assert vlist.values == [0.0, 1.0, 2.0], "Did not record values properly"
    vtuple = Vector((0, 3))
    print(vtuple)
    assert isinstance(vtuple, Vector), "Did not create with list"
    assert vtuple.values == [0.0, 1.0, 2.0], "Did not record values properly"
    vsize = Vector(3)
    print(vsize)
    assert isinstance(vsize, Vector), "Did not create with list"
    assert vsize.values == [0.0, 1.0, 2.0], "Did not record values properly"


def test_vector_add():
    v1 = Vector((4, 9))
    v2 = Vector((4, 9))
    v3 = v1 + v2
    assert v3.values == [8.0, 10.0, 12.0, 14.0, 16.0], "Did not add properly"
    v4 = v2 + v1
    assert v4.values == [8.0, 10.0, 12.0, 14.0, 16.0], "Did not add properly"
    v5 = v4 + 1
    assert v5.values == [9.0, 11.0, 13.0, 15.0, 17.0], "Did not add properly"
    v6 = 1 + v4
    assert v6.values == [9.0, 11.0, 13.0, 15.0, 17.0], "Did not add properly"


def test_vector_sub():
    v1 = Vector((4, 9))
    v2 = Vector((4, 9))
    v3 = v1 - v2
    assert v3.values == [0, 0, 0, 0, 0], "Did not sub properly"
    v4 = v2 - v1
    assert v4.values == [0, 0, 0, 0, 0], "Did not sub properly"
    v5 = v1 - 1
    assert v5.values == [3.0, 4.0, 5.0, 6.0, 7.0], "Did not sub properly"
    v6 = 1 - v1
    assert v6.values == [-3.0, -4.0, -5.0, -6.0, -7.0], "Did not sub properly"


def test_vector_div():
    v1 = Vector([12.0, 18.0])
    v3 = v1 / 3
    assert v3.values == [4.0, 6.0], "Did not div properly"
    v4 = 1 / v3
    assert v4.values == [1 / 4.0, 1 / 6.0], "Did not div properly"


def test_vector_mul():
    v1 = Vector([1.0, 2.0, 3.0])
    v2 = Vector([1.0, 2.0, 3.0])
    v3 = v1 * v2
    assert v3 == 1 * 1 + 2 * 2 + 3 * 3, "Did not sub properly"
    v4 = v2 * v1
    assert v4 == 1 * 1 + 2 * 2 + 3 * 3, "Did not sub properly"
    v5 = v1 * 2
    assert v5.values == [2.0, 4.0, 6.0], "Did not sub properly"
    v6 = 2 * v1
    assert v6.values == [2.0, 4.0, 6.0], "Did not sub properly"


def main():
    test_vector_instanciation()
    test_vector_add()
    test_vector_sub()
    test_vector_div()
    test_vector_mul()


if __name__ == "__main__":
    main()
