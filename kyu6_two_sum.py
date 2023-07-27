from itertools import permutations


def two_sum(numbers, target):
    perms = permutations(enumerate(numbers), 2)
    for ((i1, x1), (i2, x2)) in perms:
        if x1 + x2 == target:
            return [i1, i2]
