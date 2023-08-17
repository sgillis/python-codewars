from kyu6_split_strings import split_strings


def test_split_strings():
    assert ['ab', 'c_'] == split_strings('abc')
    assert ['ab', 'cd', 'ef'] == split_strings('abcdef')
