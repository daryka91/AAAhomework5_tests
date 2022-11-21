import pytest
from one_hot_encoder import fit_transform

def test_exception():
    with pytest.raises(TypeError):
        fit_transform()

def test1():
    assert fit_transform('abc') == [('abc', [1])]

def test2():
    assert fit_transform('aa', 'bb') == [('aa', [0, 1]), ('bb', [1, 0])]

def test3():
    assert fit_transform(['aa', 'aa']) == [('aa', [1]), ('aa', [1])]