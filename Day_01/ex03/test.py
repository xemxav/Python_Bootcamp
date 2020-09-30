from ex03.matrix import Matrix
from ex02.Vector import Vector


def print_matrix_info(mat, string):
    print(string)
    print("Data:", mat.data)
    print("Shape:", mat.shape)


def main():
    print_matrix_info(Matrix([[1, 2], [3, 4]]), "Init with list")
    print_matrix_info(Matrix((2,2)), "Init with tuple")
    print_matrix_info(Matrix([[1, 2], [3, 4]], (2,2)), "Init with both")
    # print_matrix_info(Matrix([[1, 2], [3, 4]], (2,3)), "Init with both & error")
    m = Matrix([[1, 2], [3, 4]])
    print_matrix_info(
        m * m, "Mul two matrice"
    )
    print_matrix_info(
        m * 2, "Mul with scalar"
    )
    print_matrix_info(
        m + m, "add two matrice"
    )
    print_matrix_info(
        m - m, "sub two matrice"
    )
    print_matrix_info(
        m / 2, "div par scalar"
    )
    vec = m * Vector([2, 5])
    print(vec.values)


if __name__ == "__main__":
    main()
