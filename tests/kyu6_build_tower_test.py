from kyu6_build_tower import build_tower


def test_duplicate_encode():
    expected = [
        "    *    ",
        "   ***   ",
        "  *****  ",
        " ******* ",
        "*********"
    ]
    assert expected == build_tower(5)
