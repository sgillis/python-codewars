def same_structure_as(original, other):
    if isinstance(original, list) and isinstance(other, list):
        if len(original) == len(other):
            for (x, y) in zip(original, other):
                if not same_structure_as(x, y):
                    return False
        else:
            return False
        return True
    elif isinstance(original, list) == isinstance(other, list):
        return True
    else:
        return False
