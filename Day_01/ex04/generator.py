import random


def generator(text, sep=" ", option=None):
    valid_option = ["ordered", "unique", "shuffle"]
    if not isinstance(text, str) \
            or option not in valid_option and option is not None:
        yield "ERROR"
    else:
        ll = text.split(sep)
        if option == valid_option[0]:
            ll.sort()
        elif option == valid_option[1]:
            ll = list(dict.fromkeys(ll))
        elif option == valid_option[2]:
            random.shuffle(ll)
        for v in ll:
            yield v


def main():
    res = generator("coucou gros comment ca va ca gros va", sep=" ",
                    option="shule")
    print(res)
    for u in generator("coucou gros comment ca va ca gros va", sep=" ",
                       option="shule"):
        print(u)


if __name__ == "__main__":
    main()
