import pytest

def test_m1():
    print("Welcome to Pytest learning")

@pytest.mark.admin
def test_m2():
    a=1
    b=0
    assert a==b

def test_m3():
    assert True

def test_m4():
    assert "PUNE" == "pune"

def test_m5():
    assert False

@pytest.mark.admin
def test_admin():
    assert 'ac'=='ac'
