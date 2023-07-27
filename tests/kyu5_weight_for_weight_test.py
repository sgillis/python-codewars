from kyu5_weight_for_weight import order_weight


def test_order_weight():
    assert "2000 103 123 4444 99" == order_weight("  103  123 4444 99 2000  ")
    assert "11 11 2000 10003 22 123 1234000 44444444 9999" == order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")
    assert "" == order_weight("")
