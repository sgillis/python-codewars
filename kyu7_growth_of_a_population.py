import math


def nb_year(p0, percent, aug, p):
    n = 0
    growth = (1 + percent / 100)
    while p0 < p:
        p0 = math.floor(p0 * growth + aug)
        n += 1
    return n
