from kyu4_nesting_structure_comparison import same_structure_as


def test_same_structure_as():
    assert same_structure_as([1, 1, 1], [2, 2, 2])
    assert same_structure_as([1, [1, 1]], [2, [2, 2]])
    assert not same_structure_as([1, [1, 1]], [[2, 2], 2])
    assert not same_structure_as([1, [1, 1]], [[2], 2])
    assert same_structure_as([[[], []]], [[[], []]])
    assert not same_structure_as([[[], []]], [[1, 1]])
