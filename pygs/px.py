import random as r
from random import randint as ri
def random():
    ls = []
    for i in range(1, 65535):
        v = ri(1, 65535)
        ls.append(v)
    return ls


def qs(ls):
    if len(ls) < 2:
        return arr
    else:
        p = ls[0]
        l = [i for i in ls[1:] if i <= p]
        g = [i for i in ls[1:] if i > p]
        return qs(l) + [p] + qs(g)


print(qs(radom()))

