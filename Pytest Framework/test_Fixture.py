import pytest


@pytest.mark.usefixtures("LoginPage")
class ATP:

    def test_SponsorsA(self, LoginPage):
        print(" Select the Sponsors1")

    def test_SponsorsB(self, LoginPage):
        print(" Select the Sponsors2")

    def test_SponsorsC(self, LoginPage):
        print(" Select the Sponsors3")

    def test_SponsorsD(self, LoginPage):
        print(" Select the Sponsors4")