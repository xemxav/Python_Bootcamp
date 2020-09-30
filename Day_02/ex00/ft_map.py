def ft_map(function_to_apply, list_of_inputs):
    ret = list()
    for elem in list_of_inputs:
        ret.append(function_to_apply(elem))
    return ret


def main():
    numbers = (1, 2, 3, 4)
    result = ft_map(lambda x: x + x, numbers)
    print(list(result))


if __name__ == "__main__":
    main()
