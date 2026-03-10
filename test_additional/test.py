import sys
sys.path.append("../src")
from math_demo import add , add_with_bug , add_something,calculate_tax


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
    add_something(10,None)==0
    add_something("1kl",10)==0

def test_calculate_tax():
    calculate_tax(1000) ==150
    calculate_tax(2000) == 300
    calculate_tax(30)==4.5
    


if __name__ == "__main__":
    test()
    test_bug_additional()
    test_addition_dublicate_logic()
    test_addition_enought()
    test_addition_overcompilate()
    test_add_something()
    
