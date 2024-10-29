# File name should start with 'test_'
# All code is wrap in 'Method'.
# 'test_FirstDemo' run file? --> Cmd--> [py.test test_CreatePolicy2 -v -s]
# 'test_CreatePolicy2' run method? --> Cmd--> [py.test -k CreatePolicy2 -v -s]
# '@pytest.mark.SmokeTestCase' (.mark) is like tagging the specific method. It helps to run Regression test cases.
# '@pytest.mark.Skip' will skip this T.C. if there ia a Major bug/No need to fix now. So, we can skip that test case.

import pytest

@pytest.mark.xfail
def test_CreatePolicy():
    print("Hi, Policy is created")


@pytest.mark.SmokeTestCase
def test_DueDate():
    print("15/1/2024")

def test_CrossBrowser(crossbrowser):
    print(crossbrowser)


