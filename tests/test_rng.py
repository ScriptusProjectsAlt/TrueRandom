from truer import TrueR

def test_randint():
    rng = TrueR()
    value = rng.randint(1, 10)
    assert 1 <= value <= 10