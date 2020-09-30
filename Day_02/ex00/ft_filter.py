def ft_filter(function_to_apply, list_of_inputs):
    ret = list()
    for elem in list_of_inputs:
        if function_to_apply(elem):
            ret.append(elem)
    return ret


def myfunc(x):
    if x < 18:
        return False
    else:
        return True


def main():
    ages = [5, 12, 17, 18, 24, 32]
    adults = filter(myfunc, ages)
    print(adults)
    adults = ft_filter(myfunc, ages)
    print(adults)


if __name__ == "__main__":
    main()
