from nltk.tokenize import sent_tokenize
from nltk import ngrams


def lines(a, b):
    """Return lines in both a and b"""

    l = set()
    a = a.split('\n')
    b = b.split('\n')

    for line in a:
        if line in b:
            l.add(line)
    return list(l)


def sentences(a, b):
    """Return sentences in both a and b"""

    l = set()
    for x in set(sent_tokenize(a)):
        if x in set(sent_tokenize(b)):
            l.add(x)
    return list(l)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    l = set()
    for x in ngrams(a, n):
        x = ''.join(x)
        if x in b:
            l.add(x)
    return list(l)
