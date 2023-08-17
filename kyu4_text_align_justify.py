# https://www.codewars.com/kata/537e18b6147aa838f600001b/train/python
from itertools import zip_longest


def pidgeon_hole(n, n_bins):
    if n_bins == 0:
        return []
    quotient = n // n_bins
    remainder = n % n_bins

    bins = [' '*quotient for i in range(n_bins)]
    for i in range(remainder):
        bins[i] += ' '
    return bins


def add_spaces(words, width):
    length = sum([len(word) for word in words])
    places = len(words) - 1
    spaces = pidgeon_hole(width - length, places)
    zipped = [x for sublist in
              [[w, s] for (w, s) in zip_longest(words, spaces, fillvalue='')]
              for x in sublist]
    return zipped[:-1]


def justify(text, width):
    words = text.split()
    line = []
    justified = []
    line_length = 0
    for word in words:
        if line == []:
            line.append(word)
            line_length += len(word) + 1
        elif line_length + len(word) <= width:
            line.append(word)
            line_length += len(word) + 1
        else:
            justified.append(line)
            line = [word]
            line_length = len(word) + 1
    justified = [add_spaces(line, width) for line in justified]
    justified.append(
        add_spaces(line, sum([len(w) for w in line]) + len(line) - 1))
    return '\n'.join([''.join(line) for line in justified])


def clever_justify(text, width):
    length = text.rfind(' ', 0, width+1)
    if length == -1 or len(text) <= width:
        return text
    line = text[:length]
    spaces = line.count(' ')
    if spaces != 0:
        expand = (width - length) // spaces + 1
        extra = (width - length) % spaces
        line = line.replace(' ', ' '*expand)
        line = line.replace(' '*expand, ' '*(expand+1), extra)
    return line + '\n' + justify(text[length+1:], width)
