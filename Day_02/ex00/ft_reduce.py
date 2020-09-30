import functools
import operator


def ft_reduce(function_to_apply, list_of_inputs):
    ll = list(list_of_inputs)
    first = ll[0]
    for elem in ll[1:]:
        first = function_to_apply(first, elem)
    return first


def main():
    lis = [1, 3, 5, 6, 2, ]
    print("The sum of the list elements is : ", end="")
    print(functools.reduce(operator.add, lis))
    print(ft_reduce(operator.add, lis))


if __name__ == "__main__":
    main()
