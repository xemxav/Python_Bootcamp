import sys


def main():
    ac = len(sys.argv)
    if ac != 2:
        print("ERROR")
        return
    arg = str(sys.argv[1])
    if arg.isdigit() is True:
        dig = int(arg)
        if dig == 0:
            print("I'm Zero.")
        elif dig % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        print("ERROR")


if __name__ == '__main__':
    main()
