
import pytest


def test_CreatePolicy2():
    a = "Policy failed"
    assert a == "Passed", "Test Case will fail"

@pytest.mark.SmokeTestCase
def test_PolicyStatus():
    print("Policy Status is in 'Active'")


def test_PaymentRef():
    print('Policy payment')


@pytest.mark.skip
def test_PolicyAmount():
    a = 200
    b = 300
    assert a == b