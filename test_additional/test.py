import sys
sys.path.append("../src")
from math_demo import add
from math_demo import test_bug_additional

def test_addition():
    assert add(2,2)==4
    print("test Addition passed")

def test_bug_additional():
    assert add_with_bug(2,2)== 4 , "function didn't returned"
    print('test Addition passed')

def test_addition_dublicate_logic():
    assert add(6,3) == 6+3
    assert add(6,3) ==9
    print("Test DUblicate passed")

def test_addition_enought():
    assert add_with_bug(2,2)==4
    assert add_with_bug(3,2)==5
    print("test_addition_enought passed!")

def test_addition_overcompilate():
    for i in range(0, 2**32):
        for j in range(0,2**32):
            assert add(i,j)==i+j

def test_add_something():
    add_something(6,3) ==9
    add_something(None,None)==0
    add_something(None,"hi")==0

if __name__ == "__main__":
    test()
    test_bug_additional()
    test_addition_dublicate_logic()
    
