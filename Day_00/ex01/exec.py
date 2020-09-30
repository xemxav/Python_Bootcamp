import sys


def main():
    argv = sys.argv
    argv.pop(0)
    for arg in argv[::-1]:
        arg = arg[::-1]
        print(arg, end=' ')


if __name__ == '__main__':
    main()
