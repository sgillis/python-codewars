from kyu4_codewars_style_ranking_system import User


def test_progress():
    user = User()
    assert user.rank == -8
    user.inc_progress(-8)
    assert user.rank == -8
    assert user.progress == 3

    user = User()
    user.inc_progress(1)
    assert user.rank == -2
    assert user.progress == 40
    user.inc_progress(1)
    assert user.rank == -2
    assert user.progress == 80
    user.inc_progress(1)
    assert user.rank == -1
    assert user.progress == 20
    user.inc_progress(1)
    assert user.rank == -1
    assert user.progress == 30
    user.inc_progress(1)
    assert user.rank == -1
    assert user.progress == 40
    user.inc_progress(2)
    assert user.rank == -1
    assert user.progress == 80
    user.inc_progress(2)
    assert user.rank == 1
    assert user.progress == 20
    user.inc_progress(-1)
    assert user.rank == 1
    assert user.progress == 21
    user.inc_progress(3)
    assert user.rank == 1
    assert user.progress == 61


def test_progress_2():
    user = User()
    user.inc_progress(-5)
    assert user.rank == -8
    assert user.progress == 90
    user.inc_progress(8)
    assert user.rank == 8
    assert user.progress == 0


def test_progress_3():
    user = User()
    user.inc_progress(-8)
    user.inc_progress(-7)
    user.inc_progress(-6)
    user.inc_progress(-5)
    user.inc_progress(-4)
    user.inc_progress(1)
    user.inc_progress(1)
    user.inc_progress(1)
    user.inc_progress(1)
    user.inc_progress(1)
    user.inc_progress(2)
    user.inc_progress(2)
    user.inc_progress(-1)
    user.inc_progress(3)
    user.inc_progress(8)
    user.inc_progress(8)
    user.inc_progress(8)
    user.inc_progress(8)
    user.inc_progress(8)
    user.inc_progress(8)
    user.inc_progress(8)
    user.inc_progress(8)
    user.inc_progress(8)
    user.inc_progress(8)
    user.inc_progress(8)
    user.inc_progress(8)
    user.inc_progress(8)
    user.inc_progress(8)
    assert user.rank == 8
    assert user.progress == 0
