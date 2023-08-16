from kyu4_hamming_numbers import hamming, fast_hamming, clever_hamming


def test_hamming():
    assert hamming(1) == 1
    assert hamming(2) == 2
    assert hamming(3) == 3
    assert hamming(4) == 4
    assert hamming(5) == 5
    assert hamming(6) == 6
    assert hamming(7) == 8
    assert hamming(8) == 9
    assert hamming(9) == 10
    assert hamming(10) == 12
    assert hamming(11) == 15
    assert hamming(12) == 16
    assert hamming(13) == 18
    assert hamming(14) == 20
    assert hamming(15) == 24
    assert hamming(16) == 25
    assert hamming(17) == 27
    assert hamming(18) == 30
    assert hamming(19) == 32


def test_fast_hamming():
    assert fast_hamming(1) == 1
    assert fast_hamming(2) == 2
    assert fast_hamming(3) == 3
    assert fast_hamming(4) == 4
    assert fast_hamming(5) == 5
    assert fast_hamming(6) == 6
    assert fast_hamming(7) == 8
    assert fast_hamming(100) == 1536
    assert fast_hamming(1000) == 51200000
    assert fast_hamming(5000) == 50837316566580


def test_clever_hamming():
    # assert clever_hamming(1) == 1
    # assert clever_hamming(2) == 2
    # assert clever_hamming(3) == 3
    # assert clever_hamming(4) == 4
    # assert clever_hamming(5) == 5
    # assert clever_hamming(6) == 6
    assert clever_hamming(7) == 8
    # assert clever_hamming(100) == 1536
    # assert clever_hamming(1000) == 51200000
    # assert clever_hamming(5000) == 50837316566580
