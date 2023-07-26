import color_ghost


def test_color_ghost():
    ghost = color_ghost.Ghost()
    assert ghost.color in ['white', 'yellow', 'purple', 'red']
