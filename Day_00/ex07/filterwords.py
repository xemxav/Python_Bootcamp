import sys
from string import punctuation as punc


def error():
    print("ERROR")
    quit(1)


def main():
    if len(sys.argv) != 3 or not sys.argv[2].isdigit():
        error()
    print([word for word in [''.join([l for l in word if l not in punc]) for word in sys.argv[1].split(' ')] if
           len(word) > int(sys.argv[2])])


if __name__ == '__main__':
    main()
