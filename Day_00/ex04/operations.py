import sys


def usage(error=""):
    if len(error) > 0:
        print("InputError:", error, end="\n\n")
    print("Usage: python operations.py <number1> <number2>")
    print("Exemple:")
    print("\tpython", sys.argv[0], "10 3")


def do_operations(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    print("{:15s}".format("Sum:"), n1 + n2)
    print("{:15s}".format("Difference:"), n1 - n2)
    print("{:15s}".format("Product:"), n1 * n2)
    if n2 != 0:
        print("{:15s}".format("Qutient:"), n1 / n2)
        print("{:15s}".format("Remainder:"), n1 % n2)
    else:
        print("{:15s}".format("Qutient:"), "ERROR (div by zero)")
        print("{:15s}".format("Remainder:"), "ERROR (modulo by zero)")


def main():
    len_a = len(sys.argv)
    if len_a == 1:
        return usage()
    if len_a > 3:
        return usage("too many arguments")
    if len_a == 2:
        return usage("need one more argument")
    n1 = sys.argv[1]
    n2 = sys.argv[2]
    if not n2.isdigit() or not n1.isdigit():
        return usage("only numbers")
    do_operations(n1, n2)


if __name__ == '__main__':
    main()
