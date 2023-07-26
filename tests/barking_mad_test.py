import barking_mad


def test_barking_mad():
    assert barking_mad.snoopy.bark() == 'Woof'
    assert barking_mad.scoobydoo.bark() == 'Woof'
