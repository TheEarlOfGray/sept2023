from functions import rando, rando2

def test_rando():
    assert rando() in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def test_rando2():
    assert rando2(5) == 10