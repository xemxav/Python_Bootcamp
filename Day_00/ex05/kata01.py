languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}


def main():
    for lang, creator in languages.items():
        print("{0} was created by {1}".format(lang, creator))


if __name__ == "__main__":
    main()
