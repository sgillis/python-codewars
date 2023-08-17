from kyu3_millionth_fibonacci import fib


def test_fib():
    assert 0 == fib(0)
    assert 1 == fib(1)
    assert 1 == fib(2)
    assert 2 == fib(3)
    assert 3 == fib(4)
    assert 5 == fib(5)
    assert 8 == fib(6)
    assert 354224848179261915075 == fib(100)
    assert 1 == fib(-1)
    assert -8 == fib(-6)
