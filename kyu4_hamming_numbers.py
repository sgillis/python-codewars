from functools import cache


@cache
def is_hamming(n):
    print(n)
    if n == 1:
        return True
    if n % 2 == 0:
        return is_hamming(n // 2)
    if n % 3 == 0:
        return is_hamming(n // 3)
    if n % 5 == 0:
        return is_hamming(n // 5)
    return False


def hamming(n):
    numbers = []
    i = 1
    while len(numbers) < n:
        if is_hamming(i):
            numbers.append(i)
        i += 1
    return numbers[-1]


def fast_hamming(n):
    i2 = 0
    i3 = 0
    i5 = 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    next_number = 1
    numbers = [1]
    for i in range(1, n):
        next_number = min(next_multiple_of_2,
                          min(next_multiple_of_3, next_multiple_of_5))
        numbers.append(next_number)
        if next_number == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = numbers[i2] * 2
        if next_number == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = numbers[i3] * 3
        if next_number == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = numbers[i5] * 5
    return next_number


def clever_hamming(n):
    bag = {1}
    for _ in range(n - 1):
        head = min(bag)
        bag.remove(head)
        bag |= {head*2, head*3, head*5}
    return min(bag)
