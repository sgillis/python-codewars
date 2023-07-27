from kyu7_growth_of_a_population import nb_year


def test_growth_of_a_population():
    assert 50 == nb_year(1500000, 0.0, 10000, 2000000)
    assert 4 == nb_year(1000, 2.0, 50, 1214)
