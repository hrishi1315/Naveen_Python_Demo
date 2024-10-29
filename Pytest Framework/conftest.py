import pytest


@pytest.fixture(scope="class")
def LoginPage():
    print("Enter username & password")
    yield
    print(" User may logout")


@pytest.fixture(params=["chrome","firefox"])
def crossbrowser(request):
    return request.param

