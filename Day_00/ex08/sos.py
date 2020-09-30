import sys

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def error():
    print("ERROR")
    quit(1)


def main():
    if len(sys.argv) < 2:
        error()
    for arg in sys.argv[1:]:
        for letter in arg:
            if not str(letter).isspace() and not str(letter).isalnum():
                error()
    ac = len(sys.argv[1:])
    for i, arg in enumerate(sys.argv[1:]):
        space = True
        for letter in arg.upper():
            if letter == ' ' and space is True:
                print('/', end=' ')
                space = False
            elif letter is not ' ':
                space = True
                print(MORSE_CODE_DICT[letter], end=" ")
        if i < ac - 1:
            print('/', end=' ')
    print("\r")


if __name__ == '__main__':
    main()
