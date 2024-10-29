import pytest

@pytest.mark.admin
def test_m6():
    assert "PUNE" == "pune"

def test_m7():
    assert False

@pytest.mark.admin
def test_admin():
    assert 'ac'=='ac'