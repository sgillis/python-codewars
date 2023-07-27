from itertools import zip_longest


def split_strings(s):
    args = [iter(s)] * 2
    zipped = zip_longest(*args, fillvalue='_')
    return [x + y for (x, y) in zipped]
