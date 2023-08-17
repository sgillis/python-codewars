def duplicate_encode(word):
    unique_chars = set(word.lower())
    translation_map = {}
    for char in unique_chars:
        count = len([c for c in word.lower() if c == char])
        if count == 1:
            replacement = '('
        else:
            replacement = ')'
        translation_map[ord(char)] = replacement
        translation_map[ord(char.upper())] = replacement
    return word.translate(translation_map)
