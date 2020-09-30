ts = (3, 30, 2019, 9, 25)


def main():
    print("{month}/{day}/{year} {hour}:{minutes}".format(month=ts[3], day=ts[4], year=ts[2], hour=ts[0], minutes=ts[1]))


if __name__ == "__main__":
    main()
