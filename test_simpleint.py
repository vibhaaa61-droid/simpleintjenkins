from simple_interest import simple_interest


def test_simple_interest():
    assert simple_interest(10000, 5, 2) == 1000


def test_simple_interest_2():
    assert simple_interest(5000, 10, 3) == 1500