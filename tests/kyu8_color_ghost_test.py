import kyu8_color_ghost


def test_color_ghost():
    ghost = kyu8_color_ghost.Ghost()
    assert ghost.color in ['white', 'yellow', 'purple', 'red']
