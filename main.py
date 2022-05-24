from sys import stderr
from panflute import *

headlines = set()


def toBold(file):
    file.replace_keyword("BOLD", Strong(Str("BOLD")))


def duplicateHeadlines(word, text):
    if type(word) == Header:
        headline = stringify(word)
        if headline in headlines:
            print("Same headlines are provided", file=stderr)
        else:
            headlines.add(headline)


def upperCase(word, text):
    if type(word) == Header and word.level > 2:
        return Header(Str(stringify(word).upper()), level=word.level)


if __name__ == "__main__":
    run_filters([duplicateHeadlines, upperCase], prepare=toBold)
