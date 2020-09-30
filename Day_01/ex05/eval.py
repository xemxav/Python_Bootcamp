class Evaluator:

    def zip_evaluate(coefs, words):
        if len(words) != len(coefs):
            return -1
        res = 0
        for w in zip(words, coefs):
            res += len(w[0]) * w[1]
        return res

    def enumerate_evaluate(coefs, words):
        if len(words) != len(coefs):
            return -1
        res = 0
        for i, coef in enumerate(coefs):
            res += len(words[i]) * coef
        return res


def main():
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.enumerate_evaluate(coefs, words))
    print(Evaluator.zip_evaluate(coefs, words))


if __name__ == "__main__":
    main()
