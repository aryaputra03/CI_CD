from src.math_op import add, sub

def test_add():
    assert add(4,5)==9
    assert add(4,1)==5
    assert add(6,5)==11

def test_sub():
    assert sub(4,5)==-1
    assert sub(4,1)==3
    assert sub(6,5)==1