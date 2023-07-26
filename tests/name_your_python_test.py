import name_your_python


def test_name_your_python():
    bubba = name_your_python.Python('Bubba')
    assert bubba.name == 'Bubba'