def order_weight(strng):
    weights = [weight for weight in strng.split(' ') if weight != '']
    sorted_weights = sorted(weights, key=lambda s: (sum(int(d) for d in s), s))
    return ' '.join(sorted_weights)
