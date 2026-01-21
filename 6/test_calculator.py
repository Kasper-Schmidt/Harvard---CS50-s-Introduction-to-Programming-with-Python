from calculator import square
import pytest

def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")








    '''
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-5) == 25
    except AssertionError:
        print("-25 squared was not 25")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")
    '''
    
    
    
    
    '''
    if square(2) != 4:
        print("2 sqaured was not 4") # Hvis jeg har n + n i stedet for n * n, vil den stadigvæk være korrekt her ved 2
    if square(3) != 3:
        print("3 sqaured was not 9")
    '''


