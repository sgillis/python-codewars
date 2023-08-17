from kyu5_finding_an_appointment import get_start_time, clever_get_start_time


def test_finding_an_appointment():
    assert '12:15' == get_start_time(schedule(), 60)
    assert get_start_time(schedule(), 90) is None


def test_clever_finding_an_appointment():
    assert '12:15' == clever_get_start_time(schedule(), 60)
    assert clever_get_start_time(schedule(), 90) is None


def schedule():
    return [
        [['09:00', '11:30'],
         ['13:30', '16:00'],
         ['16:00', '17:30'],
         ['17:45', '19:00']],
        [['09:15', '12:00'],
         ['14:00', '16:30'],
         ['17:00', '17:30']],
        [['11:30', '12:15'],
         ['15:00', '16:30'],
         ['17:45', '19:00']]
    ]
