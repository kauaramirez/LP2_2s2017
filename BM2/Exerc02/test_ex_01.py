from Main import ex01

def test_ex_01():
    assert ex01("Kaua",1500,10) == 1650
    assert ex01("Natalia", 1000, 10) == 1100
    assert ex01("Doente", 3500, 15) == 4025