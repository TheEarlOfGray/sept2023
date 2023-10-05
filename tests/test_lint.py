from lint import count

def test_count():
    assert count([1,2,2,2,2,3,4,5,6], 2) == 4
    

def test_count_2():
    assert count(["Tom", "Tim", "Tam"], "Tim") == 1