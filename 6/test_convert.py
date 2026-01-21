import pytest

from convert import convert


def test_conversion_zero():
    assert convert(0) == 0


def test_int_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000


def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691)
    assert convert(0.001) == pytest.approx(149597870.691, abs=0.1)
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2)
    


def test_convert_string():
    with pytest.raises(TypeError):
        convert("1")
        convert("dog")

