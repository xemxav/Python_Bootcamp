from string import punctuation


def text_analyzer(text="", *args, **kwargs):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if args or kwargs:
        print("ERROR")
        return
    space = 0
    ul = 0
    ll = 0
    punc = 0
    if len(text) == 0:
        return text_analyzer(input("What is the text to analyse?"))
    else:
        for i in text:
            if i.isspace():
                space += 1
            elif i in punctuation:
                punc += 1
            elif i.isupper():
                ul += 1
            if i.islower():
                ll += 1
        print("The text contains ", len(text), " charaters:", end='\n\n')
        print("-", ul, "upper letters", end='\n\n')
        print("-", ll, "lower letters", end='\n\n')
        print("-", punc, "punctuation marks", end='\n\n')
        print("-", space, "spaces")
